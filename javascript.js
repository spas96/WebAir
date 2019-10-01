$(document).ready(function () {
	"use strict"
	
	$("html,body").animate({scrollTop: 0}, 500);
	var inputBox1 = document.getElementById('adl');
	inputBox1.onchange = function(){
		inputBox1.value = inputBox1.value.replace(/[^0-9]/g, '');
	}
	var inputBox2 = document.getElementById('child');
	inputBox2.onchange = function(){
		inputBox2.value = inputBox2.value.replace(/[^0-9]/g, '');
	}
	
	var inputBox11 = document.getElementById('start_dest');
	inputBox11.onchange = function(){
		inputBox11.value = inputBox11.value.replace(/[^a-zA-Z]+$/g, '');
	}
	var inputBox22 = document.getElementById('end_dest');
	inputBox22.onchange = function(){
		inputBox22.value = inputBox22.value.replace(/[^a-zA-Z]+$/g, '');
	}
  
	$('.send-button').click(function () {
		var adl = $('#adl');
		var adl1 = adl.val();
		var child = $('#child');
		var child1 = child.val();
		var search_box_form = $('.search-box');
		var st = $('.start_dest').val();
		var end = $('.end_dest').val();
		var st1 = $('.start_date_required').val();
		var end1 = $('.end_date_required').val();			

		search_box_form.submit(function(e) {
    			e.preventDefault();
		});
		
	
		if(adl1=='0' && child1=='0'){
			
		}
		else{
			if(st!="" && end!="" && st1!="" && end1!="")
			alert("Looking for tickets..");
		}
	});

});