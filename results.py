#! /Python34/python

import cgi, cgitb, sys, mysql.connector
print("Content-type: text/html \n")

cgitb.enable()

form = cgi.FieldStorage()


radio = form.getvalue('radio') #if none -> invalid sesion search again
start_dest = form.getvalue('start_dest')
end_dest = form.getvalue('end_dest')
start_date = form.getvalue('start_date')
end_date = form.getvalue('end_date')
adl = form.getvalue('adl')
adl = int(adl)
child = form.getvalue('child')
child = int(child)
num = 0
args = (start_dest,end_dest,)
args1 = (end_dest,start_dest,)

conn = mysql.connector.connect(host='localhost',
                              database='webair',
                              user='root',
                              password='')

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


var keys = {32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1};

function preventDefault(e) {
  e = e || window.event;
  if (e.preventDefault)
      e.preventDefault();
  e.returnValue = false;  
}

function preventDefaultForScrollKeys(e) {
    if (keys[e.keyCode]) {
        preventDefault(e);
        return false;
    }
}
function disableScroll() {
  if (window.addEventListener) // older FF
      window.addEventListener('DOMMouseScroll', preventDefault, false);
  window.onwheel = preventDefault; // modern standard
  window.onmousewheel = document.onmousewheel = preventDefault; // older browsers, IE
  window.ontouchmove  = preventDefault; // mobile
  document.onkeydown  = preventDefaultForScrollKeys;
}

function enableScroll() {
    if (window.removeEventListener)
        window.removeEventListener('DOMMouseScroll', preventDefault, false);
    window.onmousewheel = document.onmousewheel = null; 
    window.onwheel = null; 
    window.ontouchmove = null;  
    document.onkeydown = null;  
} 

window.addEventListener("load", function(){
  disableScroll();
	 var load_screen = document.getElementById("load_screen");
  $("#load_screen").animate({ opacity: '0'}, 3000, function(){
   document.body.removeChild(load_screen);
   enableScroll();
  });
});
	
	function slider() {
		var obj = document.getElementById('slide'); 
		obj.style.visibility = (obj.style.visibility == 'visible') ? 'hidden' : 'visible';
		obj.style.height = (obj.style.height == '0px' || obj.style.height == '') ? '150px' : '0px';
	}

</script>
</head>


<body>


<div class="mpc_preloader" id="load_screen">
	<div class="mpc_preloader18"></div>
	<span class="mpc_preloader18_label">Loading...</span>
</div>""")



print("""

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
			<div id="main1-results">
				<div id="box">
					<div id="box-gradient-results">
					<div id="results-num"> 
""")
if conn.is_connected():
     if radio == "1":
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM journey_times WHERE jt_leave_destination = %s AND jt_arrive_destination = %s" ,args)
        row = cursor.fetchone()
        while row is not None:
           if row[5] >= (adl+child):
              num+=1
              row = cursor.fetchone()
           else:
              row = cursor.fetchone()
        cursor.close()
        print("<p>",num,"results found</p>","""	
					</div>
					</div>
											
				</div>

			</div>

			<div id="results-page">""")
        cursor1 = conn.cursor()
        cursor1.execute("SELECT * FROM journey_times WHERE jt_leave_destination = %s AND jt_arrive_destination = %s" ,args)
        row1 = cursor1.fetchone()
        while row1 is not None:
           if row1[5] >= (adl+child):
              flight_time1=row1[4]-row1[2]
              print("""<form action="results_sub.py" method="POST">
			  <input class="get_var_invisible" name="radio" value='""",radio,"""'/>
			  <input class="get_var_invisible" name="start_dest" value='""",start_dest,"""'/>
			  <input class="get_var_invisible" name="end_dest" value='""",end_dest,"""'/>
			  <input class="get_var_invisible" name="start_date" value='""",start_date,"""'/>
			  <input class="get_var_invisible" name="leave1" value='""",row1[2],"""'/>
			  <input class="get_var_invisible" name="flight_time1" value='""",flight_time1,"""'/>
			  <input class="get_var_invisible" name="arrive1" value='""",row1[4],"""'/>
			  <input class="get_var_invisible" name="seats_num" value='""",adl+child,"""'/>
     <input class="get_var_invisible" name="adl_num" value='""",adl,"""'/>
     <input class="get_var_invisible" name="child_num" value='""",child,"""'/>
     <input class="get_var_invisible" name="fare1" value='""",row1[6],"""'/>
			  <div id="empty-div">""</div>
	  		<div id="results-offer">
        <div id="results-offer-select">""")
              print("<p style='font-size:33px;'>&#163;")
              if adl >  0:
                 print(((row1[6]*adl)+(row1[6]*child-(row1[6]*child*0.2))),"</p>","<input class='get_var_invisible' name='fare' value='",((row1[6]*adl)+(row1[6]*child-(row1[6]*child*0.2))),"'/>")
              else:
                 print(row1[6]*child,"</p>","<input class='get_var_invisible' name='fare' value='",row1[6]*child,"'/>")
              print("""
            <button id="results-select-pos" class="button2">Select</button>""")
              print("<p  style='font-size:20px;'>",row1[5],"free seats</p>","""
        </div>
        <div id="results-depart">
           <p style="font-size:20px;color:red;">Depart</p><p style="font-size:18px;">""",start_dest,"-",end_dest,"</p><p style='font-size:17px;'>",start_date,"""</p> <br><br>
           <table id="table-size">
            <tr>
              <th align="left">Leave</th>
              <th align="center">Journey Time</th>
              <th align="right">Arrive</th>
            </tr>
            <tr>
              <td align="left">""",row1[2],"""</td>
              <td align="center">""",row1[4]-row1[2],"""</td>
              <td align="right">""",row1[4],"""</td>
            </tr>
           </table>
        </div>
				</div>
				</form>""")
              row1 = cursor1.fetchone()
           else:
              row1 = cursor1.fetchone()
        cursor1.close()
     else:
        cursor2 = conn.cursor(buffered=True)
        cursor2.execute("SELECT * FROM journey_times WHERE jt_leave_destination = %s AND jt_arrive_destination = %s" ,args1)
        row2 = cursor2.fetchone()
        while row2 is not None:
           cursor1 = conn.cursor()
           cursor1.execute("SELECT * FROM journey_times WHERE jt_leave_destination = %s AND jt_arrive_destination = %s" ,args)
           row1 = cursor1.fetchone()
           while row1 is not None:
              if row1[5] >= (adl+child) and row2[5] >= (adl+child):
                 num+=1
                 row1 = cursor1.fetchone()
              else:
                 row1 = cursor1.fetchone()
           cursor1.close()
           row2 = cursor2.fetchone()
        cursor2.close()
        print("<p>",num,"results found</p>","""	
					</div>
					</div>
											
				</div>

			</div>

			<div id="results-page">""")
        cursor2 = conn.cursor(buffered=True)
        cursor2.execute("SELECT * FROM journey_times WHERE jt_leave_destination = %s AND jt_arrive_destination = %s" ,args1)
        row2 = cursor2.fetchone()
        while row2 is not None:
           cursor1 = conn.cursor()
           cursor1.execute("SELECT * FROM journey_times WHERE jt_leave_destination = %s AND jt_arrive_destination = %s" ,args)
           row1 = cursor1.fetchone()
           while row1 is not None:
              if row1[5] >= (adl+child) and row2[5] >= (adl+child):
                 flight_time1=row1[4]-row1[2]
                 flight_time2=row2[4]-row2[2]
                 print("""<form action="results_sub.py" method="POST">
					<input class="get_var_invisible" name="start_dest" value='""",start_dest,"""'/>
					<input class="get_var_invisible" name="end_dest" value='""",end_dest,"""'/>
					<input class="get_var_invisible" name="start_date" value='""",start_date,"""'/>
					<input class="get_var_invisible" name="end_date" value='""",end_date,"""'/>
					<input class="get_var_invisible" name="leave1" value='""",row1[2],"""'/>
					<input class="get_var_invisible" name="leave2" value='""",row2[2],"""'/>
					<input class="get_var_invisible" name="flight_time1" value='""",flight_time1,"""'/>
					<input class="get_var_invisible" name="flight_time2" value='""",flight_time2,"""'/>
					<input class="get_var_invisible" name="arrive1" value='""",row1[4],"""'/>
					<input class="get_var_invisible" name="arrive2" value='""",row2[4],"""'/>
					<input class="get_var_invisible" name="seats_num" value='""",adl+child,"""'/>
     <input class="get_var_invisible" name="adl_num" value='""",adl,"""'/>
     <input class="get_var_invisible" name="child_num" value='""",child,"""'/>
     <input class="get_var_invisible" name="fare1" value='""",row1[6],"""'/>
     <input class="get_var_invisible" name="fare2" value='""",row2[6],"""'/>
					<div id="empty-div">""</div>
					<div id="results-offer">
					<div id="results-offer-select">
					<p  style="font-size:33px;">&#163;""")
                 if adl >  0:
                    print(((row1[6]*adl)+(row1[6]*child-(row1[6]*child*0.2)))+((row2[6]*adl)+(row2[6]*child-(row2[6]*child*0.2))),"</p>","<input class='get_var_invisible' name='fare' value='",((row1[6]*adl)+(row1[6]*child-(row1[6]*child*0.2)))+((row2[6]*adl)+(row2[6]*child-(row2[6]*child*0.2))),"'/>")
                 else:
                    print((row1[6]*child+row2[6]*child),"</p>","<input class='get_var_invisible' name='fare' value='",(row1[6]*child+row2[6]*child),"'/>")
                 print("""</p>
						<button id="results-select-pos" class="button2">Select</button>
						<p  style="font-size:20px;">""")
                 if row1[5] < row2[5]:
                    print(row1[5])
                 else:
                    print(row2[5])
                 print("""free seats</p>
					</div>
					<div style="border-bottom:1px solid #636363;" id="results-depart">
						<p style="font-size:20px;color:red;">Depart</p><p style="font-size:18px;">""",start_dest,"-",end_dest,"</p><p style='font-size:17px;'>",start_date,"""</p> <br><br>
						<table id="table-size">
						  <tr>
							<th align="left">Leave</th>
							<th align="center">Journey Time</th>
							<th align="right">Arrive</th>
						  </tr>
						  <tr>
							<td align="left">""",row1[2],"""</td>
							<td align="center">""",row1[4]-row1[2],"""</td>
							<td align="right">""",row1[4],"""</td>
						  </tr>
						</table>
					</div>
					<div id="results-depart">
						<p style="font-size:20px;color:red;">Return</p><p style="font-size:18px;">""",end_dest,"-",start_dest,"</p><p style='font-size:17px;'>",end_date,"""</p> <br><br>
						<table id="table-size">
						  <tr>
							<th align="left">Leave</th>
							<th align="center">Journey Time</th>
							<th align="right">Arrive</th>
						  </tr>
						  <tr>
							<td align="left">""",row2[2],"""</td>
							<td align="center">""",row2[4]-row2[2],"""</td>
							<td align="right">""",row2[4],"""</td>
						  </tr>
						</table>
					</div>
				</div>
				</form>""")
                 row1 = cursor1.fetchone()
              else:
                 row1 = cursor1.fetchone()
           cursor1.close()
           row2 = cursor2.fetchone()
        cursor2.close()
     print("""
					<div id="empty-div">""</div>
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
</html>""")
conn.close()