# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#    See LICENSE file for full copyright and licensing details.
#################################################################################
import werkzeug.utils
import werkzeug.wrappers
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)
from odoo import http, _
from odoo.addons.auth_signup.models.res_users import SignupError
from odoo.addons.web.controllers.main import ensure_db, Home
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.addons.website_sale.controllers.main   import WebsiteSale


class ReferEarnSignup(AuthSignupHome):


	def getReferralCode(self,user,referral,referral_code):
		
		if referral_code:
			checkparentReferral = user.partner_id._createReferralAccount(
				partner_id=user.partner_id.id,
				parent_referral_code= referral_code,
				user_id=user.id
				)
			
			
			if referral and referral == referral_code:
				user.partner_id.is_direct = False
			else:
				user.partner_id.is_direct = True

			if checkparentReferral['is_parent_referral']:
				request.env['transaction.history'].sudo()._createTransactionSignup(
					partner_id = user.partner_id.id,
					user_id = user.id,
					parent_user_id = checkparentReferral['parent_user_id']
					)
			else:
				request.env['transaction.history'].sudo()._createInvalidTransactionSignup(
					user_id = user.id,
					invalid_referal= referral_code
					)

		else:
			ReferralCustomer = user.partner_id._createReferralAccount(
				partner_id=user.partner_id.id,
				parent_referral_code="",
				user_id=user.id
				)


	@http.route('/referral/submit',type='json', auth='public',website=True)
	def referral_submit(self,referral='',**kw):
		referral_code = referral
		
		user = request.env.user
		if user.referral_code_used_bool:
			return {'error':"You have already used someone's referral code"}
		checkparentReferral = user.partner_id._createReferralAccount(
				partner_id=user.partner_id.id,
				parent_referral_code= referral_code,
				user_id=user.id
				)
		if checkparentReferral.get('is_parent_referral'):
			self.getReferralCode(user,referral,referral_code)
			request.env.user.referral_code_used_bool = True
			return True
		return {'error':'Invalid Referral Code.'}
		
			

	@http.route('/web/signup', type='http', auth='public', website=True)
	def web_auth_signup(self, *args, **kw):
		referral = request.httprequest.args.get('referral')
		result = super(ReferEarnSignup, self).web_auth_signup(*args, **kw)
		
		result.qcontext.update({
			'referral':referral
			})
		
		if result.qcontext.get('error'):
			return result
		else:
			user = request.env.user
			if request.httprequest.method == 'POST':
				self.getReferralCode(user,referral,kw.get('referral'))
			return result


class ReferEarnWebsiteSale(WebsiteSale):

	@http.route(['/shop/confirmation'], type='http', auth="public", website=True)
	def shop_payment_confirmation(self, **post):
		result = super(ReferEarnWebsiteSale, self).shop_payment_confirmation(**post)
		user = request.env.user
		checkComsnType = request.env['res.config.settings'].sudo().get_values().get('verify_commission') == 'afterOrder'
		if checkComsnType and result.qcontext.get('order'):
			order = request.env['sale.order'].sudo().search([('partner_id','=',user.partner_id.id)])
			if len(order) == 1:
				TxnObj = request.env['transaction.history'].sudo()
				if order.state == 'sale':
					TxnObj.addComsnOnFirstSale(user_id=user.id,first_order=order.id)
					# addComsnOnFirstSale() this methods runs when payment gateway is used and
					# sale order is directly converted to state 'sale'
				else:
					TxnObj.addFirstOrderTransaction(user_id=user.id,first_order=order.id)


		return result


	@http.route('/shop/payment/validate', type='http', auth="public", website=True)
	def shop_payment_validate(self, transaction_id=None, sale_order_id=None, **post):
		""" Method that should be called by the server when receiving an update
		for a transaction. State at this point :

		 - UDPATE ME
		"""
		user = request.env.user
		if sale_order_id is None:
			last_saleOrder = request.website.sale_get_order()
		else:
			last_saleOrder = request.env['sale.order'].sudo().browse(sale_order_id)
			assert order.id == request.session.get('sale_last_order_id')
		if last_saleOrder.use_re_epoints and user.partner_id.referral_earning > 0.0:
			request.env['transaction.history'].sudo()._create_ReferaldebitTransaction(
				user_id=user.id ,
				amount=last_saleOrder.redeemable_points,
				order_id=last_saleOrder.id,
				order_name=last_saleOrder.name
				)
		result = super(ReferEarnWebsiteSale,self).shop_payment_validate(transaction_id, sale_order_id, **post)
		return result
