/* Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>) */
/* See LICENSE file for full copyright and licensing details. */
odoo.define('refer_and_earn.custom',function(require){
"use strict";

var core = require('web.core');
var ajax = require('web.ajax');

var _t = core._t;

// COPY TO CLIPBOARD

  $(document).ready(function() {

    
    $('#refferal_code_button').click(function(){
      $('.alert_none').addClass('d-none');
      $('#referral_input_id').val('');
    })
    
    $('#reffered_code_id').submit(function(ev){
      ev.preventDefault();
      console.log($('.alert_none'))
      var referral = $(ev.currentTarget).find('input').val();
      ajax.jsonRpc("/referral/submit",'call',{referral:referral}).then(function(response){
        if (response.error){
          $('.alert_none').removeClass('d-none').text(response.error);
        }
        else{
          window.location.href='/my/refer_earn'
        } 
        
        
      })
      // console
      
    });
    

  	$("#referral_label").click(function(){
      $("#referral_input").toggle();
     
    });


    $("#copy_referral").click(function(){
      $("#referral_code").select();
      document.execCommand('copy');
    });



    $('#use_referal_earning').on('change',function(){
		$.loader({
	    	className:"blue-with-image-2",
	    	content:'please wait ...'
		});
     var used_earnings = $('#use_referal_earning').is(':checked')		
	    ajax.jsonRpc("/payment/referralEarning", 'call',{'used_earnings': used_earnings}).then(function (result){
	        if (result)
	          location.reload();
	         else
	           location.reload();
	    });

    });
  });




});


