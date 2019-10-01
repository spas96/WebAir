#! /Python34/python

import cgi, cgitb, sys, mysql.connector, datetime
from datetime import date
print("Content-type: text/html \n")

cgitb.enable()

form = cgi.FieldStorage()

now = datetime.datetime.now()
y = now.year
mon = now.month
d = now.day
h = now.hour
min = now.minute
s = now.second

ticket_id = form.getvalue('ticket_id')
ticket_id = int(ticket_id)

conn = mysql.connector.connect(host='localhost',
                              database='webair',
                              user='root',
                              password='')


if conn.is_connected():
   cursor = conn.cursor()
   query = """SELECT * FROM `tickets` WHERE id = """+str(ticket_id)
   cursor.execute(query)
   row = cursor.fetchone()
   cursor.close()
   cursor1 = conn.cursor()
   query1 = """SELECT AUTO_INCREMENT
               FROM information_schema.TABLES
               WHERE TABLE_SCHEMA = "webair"
               AND TABLE_NAME = "tickets" """
   cursor1.execute(query1)
   row1 = cursor1.fetchone()
   row1 = str(row1)
   row1 = row1.replace("(", "")
   row1 = row1.replace(")", "")
   row1 = row1.replace(",", "")
   row1 = int(row1)
   cursor1.close()
   
      



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
   """)
if ticket_id<row1 and ticket_id > 0:
   print("""
   <form action="manage_ticket_cancel.py" method="POST">
     <H1>Cancel your ticket</H1>
     <p style="margin-left:20px;font-size:18px;">Id:"""+str(row[0]),"""Email:"""+row[1],"""Name:"""+row[2],row[3],"""Seat number:"""+str(row[4]),"""Destination:"""+row[5],"""</p>
     </br>
     </br>
     <input class="get_var_invisible" name="id" value='"""+str(row[0])+"""'/>
     <input class="get_var_invisible" name="email" value='"""+row[1]+"""'/>
     <input class="get_var_invisible" name="name" value='"""+row[2]+"""'/>
     <input class="get_var_invisible" name="surname" value='"""+row[3]+"""'/>
     <input class="get_var_invisible" name="seat" value='"""+str(row[4])+"""'/>
     <input class="get_var_invisible" name="dest" value='"""+row[5]+"""'/>
     <input class="get_var_invisible" name="depart" value='"""+row[13]+"""'/>
     <input class="get_var_invisible" name="return_" value='"""+row[14]+"""'/>
     <input class="get_var_invisible" name="days_dif" value='"""+str(row[15])+"""'/>
     <button style="left:110;" id="cancel_ticket" class="button3">Cancel ticket</button>
   </form>""")
else:
   print("""<p style="margin-left:20px;font-size:18px;">No ticket with this ID!</p>""")
print("""
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