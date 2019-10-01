#! /Python34/python

import cgi, cgitb, sys, mysql.connector
print("Content-type: text/html \n")

cgitb.enable()

form = cgi.FieldStorage()



conn = mysql.connector.connect(host='localhost',
                              database='webair',
                              user='root',
                              password='')


#if conn.is_connected():



print("""
<html>
<head>
  <meta charset="utf-8">

<link rel="StyleSheet" href="try.css" type="text/css" media="screen">
<script type="text/javascript" src="http://code.jquery.com/jquery-1.7.2.min.js"></script>


<script>
$(document).ready(function () {
	"use strict"
	
	$("html,body").animate({scrollTop: 0}, 500);

})
window.addEventListener("load", function(){
	var load_screen = document.getElementById("load_screen");
	$("#load_screen").animate({ opacity: '0'}, 3000, function(){
	document.body.removeChild(load_screen);
	});
	});
	
	function slider() {
		var obj = document.getElementById('slide'); 
		obj.style.visibility = (obj.style.visibility == 'visible') ? 'hidden' : 'visible';
		obj.style.height = (obj.style.height == '0px' || obj.style.height == '') ? '150px' : '0px';
	}
 
function get_ticket_id(){
   var obj = document.getElementById('ticketid').value; 
   document.getElementById('ticket_id').value = obj;
}

</script>
<script>
jQuery(function($){ //on document.ready
Object.defineProperty(Array.prototype, "remove", {
    enumerable: false,
    value: function (itemToRemove) {
        var removeCounter = 0;

        for (var index = 0; index < this.length; index++) {
            if (this[index] == itemToRemove) {
                this.splice(index, 1);
                removeCounter++;
                index--;
            }
        }
        return removeCounter;
    }
});

})



 
</script>
</head>


<body>


<div class="mpc_preloader" id="load_screen">
	<div class="mpc_preloader18"></div>
	<span class="mpc_preloader18_label">Loading...</span>
</div>

	<div id="wrapper">
		<div id="header">

		<div id="main1-left-clamp-results">
		
			<div id="clamp-gradient">
			</div>
		
		</div>
		
		<div id="main1-right-clamp-results">
		
			<div id="clamp-gradient">
			</div>
		
		</div>
			<div id="box-shadow"></div>
			<div id="header-gradient">
			
				<div id="header-position">
					
					<form>
						<a href="/webprog/WebAir/" id="home" style="border-bottom: 1px solid #e02e36;" class="button-top">Home</a>
						<a href="#" id="info" class="button-top">Flights Info</a>
						<a href="/webprog/WebAir/manage_ticket.py" id="manage" class="button-top">Manage Ticket</a>
						<a href="#" id="about" class="button-top">About Us</a>
					</form>
					
				</div>
				<p class="account" onclick="slider();">Account</p>
			</div>
		<div id="logo-box">
			<img src="http://i67.tinypic.com/f6w5i.png" style="width:100%;height:100%;">
		</div>
		</div>

			<div id="results-page" style="margin-top:62px;">
   <form action="manage_ticket_result.py" method="POST">
     <H1>Cancel your ticket</H1>
     <H2 style="margin-left:20px;">Enter your ticket id:</H2>
     <input style="margin-left:20px;" class="name" onchange="get_ticket_id()" type="text" id="ticketid"  placeholder= "Ticket ID"  required/>
     </br>
     </br>
     <input class="get_var_invisible" name="ticket_id" id="ticket_id" value=''/>
     <button style="left:110;" id="cancel_ticket" class="button3">Find ticket</button>
   </form>
			</div>
		<div id="footer">
		<div id="box-shadow"></div>
			<div id="header-gradient">
				<div id="footer-position">
					&#174 2016 UWE WebAir. All rights reserved. 
				</div>
			</div>

		</div>
		<div id="slide" class="slide">
	  		<div id="logo-box">
				<form>
					<p style="font-size:13px;">Sign in to see exclusive Member Pricing</p>
					<button class="button1">Sign in</button>
					<p>New? <a href="url" style="color:red;">Create an Account</a></p>
				</form>
			</div>
		</div>
    </div>
</body>
</html>
""")
conn.close()