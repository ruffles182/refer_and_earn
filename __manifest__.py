# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################
{
  "name"                 :  "Website Refer And Earn",
  "summary"              :  """Odoo Website Refer And Earn allows your customers to refer your business to their friends and earn Bonus Points.""",
  "category"             :  "Website",
  "version"              :  "1.1.4",
  "sequence"             :  1,
  "author"               :  "Webkul Software Pvt. Ltd.",
  "license"              :  "Other proprietary",
  "maintainer"           :  "Saurabh Gupta",
  "website"              :  "https://store.webkul.com/Odoo-Website-Refer-And-Earn.html",
  "description"          :  """Odoo Website Refer And Earn
Website Refer And Earn
Referral Points
Refer And Earn
Refer And Earn in Odoo Website
Earn Referral Points
Refer
Refer to your friends
Referral Bonus
Refer a friend""",
  "live_test_url"        :  "http://odoodemo.webkul.com/?module=refer_and_earn&lifetime=90&lout=1&custom_url=/refer_earn/",
  "depends"              :  [
                             'auth_oauth',
                             'sales_team',
                             'website_sale',
                             'web',
                             'web_tour',
                            ],
  "data"                 :  [
                             'security/ir.model.access.csv',
                             'data/sequence_data.xml',
                             'views/transaction_history_view.xml',
                             'views/res_partner_view.xml',
                             'views/res_users_view.xml',
                             'views/homepage_template.xml',
                             'views/res_config_views.xml',
                             'views/menus_view.xml',
                             'views/header_footer_template.xml',
                             'views/my_referEarn_template.xml',
                             'views/refer_earn_stats_template.xml',
                             'views/inherit_shop_payment_template.xml',
                             'views/refer_earn_signup_view.xml',
                             'views/sale_order_inherit_view.xml',
                             'views/wizard_landing_content_view.xml',
                            ],
  "assets"               : {'web.assets_frontend':["/refer_and_earn/static/src/css/website_refer_and_earn.css",
                                                  "/refer_and_earn/static/loader/jquery.loader.css",
                                                  # "/refer_and_earn/static/src/js/chart-loader.js",
                                                  "/refer_and_earn/static/src/js/custom-chart-loader.js",
                                                  "/refer_and_earn/static/src/js/custom.js",
                                                  "/refer_and_earn/static/src/js/my.js",
                                                  "/refer_and_earn/static/loader/jquery.loader.js"
                                                  ]

                            },
  "demo"                 :  ['data/demo_data_view.xml'],
  "images"               :  ['static/description/Banner.gif'],
  "application"          :  True,
  "installable"          :  True,
  "price"                :  99,
  "currency"             :  "USD",
  'pre_init_hook'        :'pre_init_check'
}
