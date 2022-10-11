/* Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>) */
/* See LICENSE file for full copyright and licensing details. */
odoo.define('refer_and_earn.wk_refer_account',function(require){
"use strict";

var core = require('web.core');
// var ajax = require('web.ajax');

var _t = core._t;

  $(document).ready(function() {
    var mat = $('#matrix').val().split("-");
  //   function drawChart() {
  //     if($('#matrix').length){
  //       var mat = $('#matrix').val().split("-");
  //     // else
  //     //  var mat = 0;
  //     var data = google.visualization.arrayToDataTable([
  //       ['State', 'total state types'],
  //       ['Approved',  parseInt(mat[4])],
  //       ['Pending',     parseInt(mat[0])],
  //       ['Error',     parseInt(mat[1])],
  //       ['Rejected',  parseInt(mat[2])],
  //       ['Cancel',    parseInt(mat[3])],
  //       ['No Referral Stat',  parseInt(mat[5])],
  //     ]);
      
  //     var options = {
  //       title:' ',
  //       pieSliceTextStyle: {
  //         color: 'black',
  //       },
  //       pieHole: 0.4,
  //       colors : ['#337ab7','#ec971f','#3c763d','red','#b733ad','grey'],
  //     };
  //     var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
  //     chart.draw(data, options);
  //   }
  // }
  //   google.charts.load("visualization", "1",{packages:["corechart"]});
  //   google.charts.setOnLoadCallback(drawChart);




    var xValues = ['Approved', 'Pending','Error', 'Rejected', 'Cancel','No Referral Stat'];
    var yValues = [parseInt(mat[4]), parseInt(mat[0]), parseInt(mat[1]), parseInt(mat[2]), parseInt(mat[3]),parseInt(mat[5])];
    var barColors =  ['#337ab7','#ec971f','#3c763d','red','#b733ad','grey']

    new Chart("myChart", {
      type: "doughnut",
      data: {
        labels: xValues,
        datasets: [{
          backgroundColor: barColors,
          data: yValues
        }]
      },
      options: {
        title: {
          display: true,
          // text: "World Wide Wine Production 2018"
        }
      }
    });
  });

});