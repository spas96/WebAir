#! /Python34/python

import cgi, cgitb, sys, mysql.connector,datetime,time
from datetime import date,timedelta
print("Content-type: text/html \n")

cgitb.enable()

form = cgi.FieldStorage()

radio=form.getvalue('radio')
start_dest=form.getvalue('start_dest')
end_dest=form.getvalue('end_dest')
start_date=form.getvalue('start_date')
leave1=form.getvalue('leave1')
flight_time1=form.getvalue('flight_time1')
arrive1=form.getvalue('arrive1')
fare=form.getvalue('fare')
fare1=form.getvalue('fare1')
seats_num=form.getvalue('seats_num')
adl=form.getvalue('adl_num')
child=form.getvalue('child_num')
l1=leave1.strip()
coll1=str(start_dest+"-"+end_dest+"- "+l1).strip()
dest1=str(start_dest+"-"+end_dest).strip()

now = datetime.datetime.now()
year = datetime.datetime.today().year
st_date = datetime.datetime.strptime(start_date, ' %m/%d/%Y ')
fromdate = date(now.year,now.month,now.day)
todate = date(st_date.year,st_date.month,st_date.day)
daygenerator = (fromdate + timedelta(x + 1) for x in range((todate - fromdate).days))
days_from_today=sum(1 for day in daygenerator if day.weekday() > 0)
days_dif1 = days_from_today


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

function calladl(day,month,year) {
var kcyear = document.getElementsByName(year)[0],
    kcmonth = document.getElementsByName(month)[0],
    kcday = document.getElementsByName(day)[0];
var d = new Date();
var n = d.getFullYear();
var nm = d.getMonth();
var nd = d.getDate();
for (var i = n-10; i >= n-100; i--) {
    var opt = new Option();
    opt.value = opt.text = i;
    kcyear.add(opt);
}
kcyear.addEventListener("change", validate_date1);
kcmonth.addEventListener("change", validate_date1);
kcday.addEventListener("change", validate_date1);

function validate_date1() {
var y = +kcyear.value,
    m = kcmonth.value,
    d = kcday.value;   
if (m === "2") var mlength = 28 + (!(y & 3) && ((y % 100) !== 0 || !(y & 15)));
else var mlength = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1];
kcday.length = 1;
    for (var i = 1; i <= mlength; i++) {
        var opt = new Option();
        opt.value = opt.text = i;
        if (i == d) opt.selected = true;
        kcday.add(opt);
    }
}
            validate_date1();
}

function callchild(error2,day2,month2,year2,errcheck) {
var kcyear = document.getElementsByName(year2)[0],
    kcmonth = document.getElementsByName(month2)[0],
    kcday = document.getElementsByName(day2)[0];
    err = document.getElementsByName(error2) [0];
    errcheck1 = document.getElementsByName(errcheck) [0];
var d = new Date();
var n = d.getFullYear();
var nm = d.getMonth();
var nd = d.getDate();
for (var i = n; i >= n-10; i--) {
    var opt = new Option();
    opt.value = opt.text = i;
    kcyear.add(opt);
}
kcyear.addEventListener("change", validate_date2);
kcmonth.addEventListener("change", validate_date2);
kcday.addEventListener("change", validate_date2);

function validate_date2() {
var y = +kcyear.value,
    m = kcmonth.value,
    d = kcday.value;   
if (m === "2") var mlength = 28 + (!(y & 3) && ((y % 100) !== 0 || !(y & 15)));
else var mlength = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1];
kcday.length = 1;
    for (var i = 1; i <= mlength; i++) {
        var opt = new Option();
        opt.value = opt.text = i;
        if (i == d) opt.selected = true;
        kcday.add(opt);
    }

if ((y>=n && m>nm+1) || (y>=n && m==nm+1 && d>nd)){
     err.innerHTML ="Invalid date";
     errcheck1.value = "";
}
else
{
   err.innerHTML ="";
   errcheck1.value = " ";
}
}
            validate_date2();
}

var numofadl = """,int(adl),""";
var numofchild = """,int(child),""";
var adultsname = [];
var adultssurname = [];
var childsname = [];
var childssurname = [];
for(var i = 0; i < numofadl; i++) {
    adultsname.push("");
    adultssurname.push("");
}
for(var i = 0; i < numofchild; i++) {
    childsname.push("");
    childssurname.push("");
}

function nameinarr1(id1) {
   var name1 = document.getElementById("name1 "+id1+" ").value;
   var surname1 = document.getElementById("surname1 "+id1+" ").value;
   adultsname[id1-1] = name1;
   adultssurname[id1-1] = surname1;
   connectnamearr();
}
function nameinarr2(id2) {
   var name2 = document.getElementById("name2 "+id2+" ").value;
   var surname2 = document.getElementById("surname2 "+id2+" ").value;
   childsname[id2-1] = name2;
   childssurname[id2-1] = surname2;
   connectnamearr();
}

function connectnamearr() {
   var names = adultsname+","+childsname;
   var surnames = adultssurname+","+childssurname;
   document.getElementById("names").value = names;
   document.getElementById("surnames").value = surnames;
}


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
       var arr1 = [];
       var arr2 = [];
       var max_seats1 = """,seats_num,""";
       var max_seats2 = """,seats_num,""";
       var seats1 = [], i = 121;
       var seats_first = 0;
       var array1 = $("#array1").val();
         while (i--) {
           seats1[i] = 1;
         }
       """)
for num1 in range(1,121):
   print("""
       $('#'+""",num1,""").click(function() {
        seats_first=""",num1,"""


        if(seats1[""",num1,"""]%2 != 0){""")
   if radio == " 1 ":
      print("""
         if(max_seats1==0){
          alert("You chose seats for all passengers! To reorder it first deselect seat and then chose another!");
         }""")
   else:
      print("""
         if(max_seats1==0 && max_seats2==0){
          alert("You chose seats for all passengers! To reorder it first deselect seat and then chose another!");
         }
         if(max_seats1==0 && max_seats2!=0 && seats_first<61){
          alert("You chose seats for all passengers for 1st flight! To reorder it first deselect seat and then chose another!");
         }
         if(max_seats1!=0 && max_seats2==0 && seats_first>60 && seats_first<121){
          alert("You chose seats for all passengers for 2nd flight! To reorder it first deselect seat and then chose another!");
         }
         """)
   print("""
         if(max_seats1>0 && seats_first<61){
          seats1[""",num1,"""]+=1;
          this.style.backgroundColor = "orange";
          max_seats1--;
          arr1.push(this.id);
         if(max_seats1==0){
            document.getElementById('seatmincheck').value = " ";
         }
         else{
            document.getElementById('seatmincheck').value = "";
         }
         }
         if(max_seats2>0 && seats_first>60 && seats_first<121){
          seats1[""",num1,"""]+=1;
          this.style.backgroundColor = "orange";
          max_seats2--;
          arr2.push(this.id-60);
          if(max_seats2==0){
             document.getElementById('seatmincheck1').value = " ";
          }
          else{
             document.getElementById('seatmincheck1').value = "";
          }
         }
        }
        else{
         if(seats_first<61){
          this.style.backgroundColor = "#4CAF50";
          seats1[""",num1,"""]+=1;
          arr1.remove(this.id);
          max_seats1++;
         if(max_seats1==0){
            document.getElementById('seatmincheck').value = " ";
         }
         else{
            document.getElementById('seatmincheck').value = "";
         }
         }
         else{
          this.style.backgroundColor = "#4CAF50";
          seats1[""",num1,"""]+=1;
          arr2.remove(this.id);
          max_seats2++;
         if(max_seats2==0){
            document.getElementById('seatmincheck1').value = " ";
         }
         else{
            document.getElementById('seatmincheck1').value = "";
         }
         }
        }
        $('#array1').val(arr1);
        $('#array2').val(arr2);
        //alert(arr1);
        //alert(arr2);
       })
      """)
print("""


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
			<div id="main1-results">
				<div id="box">
					<div id="box-gradient-results">
					<div id="results-num">
						<p>Passangers and seats</p>
					</div>
					</div>				
				</div>
			</div>""")
if conn.is_connected():
   print("""<div id="results-page">
   <form action="payment.py" method="POST">
   """)
   
   if radio==" 1 ":
 
      
      print("""
				<div id="empty-div" style="opacity:0">""</div>
				<H2 style="margin-left:20px;">Journey</H2>
	  			<div id="results-offer">
					<div id="results-offer-select">
						<p style='font-size:33px;'>&#163;""",fare,"""</p>
					</div>
					<div id="results-depart">
						<p style="font-size:20px;color:red;">Depart</p><p style="font-size:18px;">""",start_dest,'-',end_dest,"""</p><p style='font-size:17px;'>""",start_date,"""</p> <br><br>
						<table id="table-size">
						  <tr>
							<th align="left">Leave</th>
							<th align="center">Journey Time</th>
							<th align="right">Arrive</th>
						  </tr>
						  <tr>
							<td align="left">""",leave1,"""</td>
							<td align="center">""",flight_time1,"""</td>
							<td align="right">""",arrive1,"""</td>
						  </tr>
						</table>
					</div>
				</div>
    <input id='seatmincheck' name='seatmincheck' style="position:absolute;margin-top:100px;margin-left:-45px;z-index:-900;opacity:0;" required/>
				<H2 style="margin-top:100px;margin-left:20px;">Choose your seats</H2>
				<div id="col_legend1" style="margin-left:20px;">
						<div id="col1">
							<p id="spacing_last">Legend</p>
						</div>
						<div id="col_legend">
							<p>
								<a class="button_seats button_green button_about" style="pointer-events: none;"></a
							</p>
						</div>
						<div id="col_legend">
							<p>
								<a class="button_seats button_green button_about" style="pointer-events: none;background-color:red;"></a>
							</p>
						</div>
						<div id="col_legend">
							<p>
								<a class="button_seats button_green button_about" style="pointer-events: none;background-color:orange;"></a>
							</p>
						</div>
				</div>
				<div id="col_num">
						<div id="col1_lt" style="margin-top:45px">
							<p id="spacing_last">Seat is free</p>
						</div>
						<div id="col1_lt">
							<p id="spacing_last">Seat is occupied</p>
						</div>
						<div id="col1_lt">
							<p id="spacing_last">Selected seat</p>
						</div>
					</div>
				<div id="seats">
					<div id="col">
						<div id="col1">
							<p id="spacing">A B C</p>
						</div>
						<div id="col1">
							<p>
								<a id="1" """)
      cursor1 = conn.cursor()
      cursor1.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(1,))
      row1 = cursor1.fetchone()
      while row1 is not None:
         if row1[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row1 = cursor1.fetchone()
         else:
            row1 = cursor1.fetchone()
         print("""
         class="button_seats button_green button_about"></a>
								<a id="2" """)
      cursor2 = conn.cursor()
      cursor2.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(2,))
      row2 = cursor2.fetchone()
      while row2 is not None:
         if row2[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row2 = cursor2.fetchone()
         else:
            row2 = cursor2.fetchone()
         print("""class="button_seats button_green button_about"></a>
								<a id="3" """)
      cursor3 = conn.cursor()
      cursor3.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(3,))
      row3 = cursor3.fetchone()
      while row3 is not None:
         if row3[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row3 = cursor3.fetchone()
         else:
            row3 = cursor3.fetchone()
         print("""class="button_seats button_green button_about"></a>
							</p>
						</div>
						<div id="col1">
							<p>
								<a id="4" """)
      cursor4 = conn.cursor()
      cursor4.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(4,))
      row4 = cursor4.fetchone()
      while row4 is not None:
         if row4[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row4 = cursor4.fetchone()
         else:
            row4 = cursor4.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="5" """)
      cursor5 = conn.cursor()
      cursor5.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(5,))
      row5 = cursor5.fetchone()
      while row5 is not None:
         if row5[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row5 = cursor5.fetchone()
         else:
            row5 = cursor5.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="6" """)
      cursor6 = conn.cursor()
      cursor6.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(6,))
      row6 = cursor6.fetchone()
      while row6 is not None:
         if row6[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row6 = cursor6.fetchone()
         else:
            row6 = cursor6.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="7" """)
      cursor7 = conn.cursor()
      cursor7.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(7,))
      row7 = cursor7.fetchone()
      while row7 is not None:
         if row7[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row7 = cursor7.fetchone()
         else:
            row7 = cursor7.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="8" """)
      cursor8 = conn.cursor()
      cursor8.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(8,))
      row8 = cursor8.fetchone()
      while row8 is not None:
         if row8[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row8 = cursor8.fetchone()
         else:
            row8 = cursor8.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="9" """)
      cursor9 = conn.cursor()
      cursor9.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(9,))
      row9 = cursor9.fetchone()
      while row9 is not None:
         if row9[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row9 = cursor9.fetchone()
         else:
            row9 = cursor9.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="10" """)
      cursor10 = conn.cursor()
      cursor10.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(10,))
      row10 = cursor10.fetchone()
      while row10 is not None:
         if row10[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row10 = cursor10.fetchone()
         else:
            row10 = cursor10.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="11" """)
      cursor11 = conn.cursor()
      cursor11.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(11,))
      row11 = cursor11.fetchone()
      while row11 is not None:
         if row11[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row11 = cursor11.fetchone()
         else:
            row11 = cursor11.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="12" """)
      cursor12 = conn.cursor()
      cursor12.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(12,))
      row12 = cursor12.fetchone()
      while row12 is not None:
         if row12[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row12 = cursor12.fetchone()
         else:
            row12 = cursor12.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="13" """)
      cursor13 = conn.cursor()
      cursor13.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(13,))
      row13 = cursor10.fetchone()
      while row13 is not None:
         if row13[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row13 = cursor13.fetchone()
         else:
            row13 = cursor13.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="14" """)
      cursor14 = conn.cursor()
      cursor14.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(14,))
      row14 = cursor14.fetchone()
      while row14 is not None:
         if row14[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row14 = cursor14.fetchone()
         else:
            row14 = cursor14.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="15" """)
      cursor15 = conn.cursor()
      cursor15.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(15,))
      row15 = cursor15.fetchone()
      while row15 is not None:
         if row15[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row15 = cursor15.fetchone()
         else:
            row15 = cursor15.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="16" """)
      cursor16 = conn.cursor()
      cursor16.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(16,))
      row16 = cursor16.fetchone()
      while row16 is not None:
         if row16[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row16 = cursor16.fetchone()
         else:
            row16 = cursor16.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="17" """)
      cursor17 = conn.cursor()
      cursor17.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(17,))
      row17 = cursor17.fetchone()
      while row17 is not None:
         if row17[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row17 = cursor17.fetchone()
         else:
            row17 = cursor17.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="18" """)
      cursor18 = conn.cursor()
      cursor18.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(18,))
      row18 = cursor18.fetchone()
      while row18 is not None:
         if row18[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row18 = cursor18.fetchone()
         else:
            row18 = cursor18.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="19" """)
      cursor19 = conn.cursor()
      cursor19.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(19,))
      row19 = cursor19.fetchone()
      while row19 is not None:
         if row19[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row19 = cursor19.fetchone()
         else:
            row19 = cursor19.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="20" """)
      cursor20 = conn.cursor()
      cursor20.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(20,))
      row20 = cursor20.fetchone()
      while row20 is not None:
         if row20[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row20 = cursor20.fetchone()
         else:
            row20 = cursor20.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="21" """)
      cursor21 = conn.cursor()
      cursor21.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(21,))
      row21 = cursor21.fetchone()
      while row21 is not None:
         if row21[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row21 = cursor21.fetchone()
         else:
            row21 = cursor21.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="22" """)
      cursor22 = conn.cursor()
      cursor22.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(22,))
      row22 = cursor22.fetchone()
      while row22 is not None:
         if row22[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row22 = cursor22.fetchone()
         else:
            row22 = cursor22.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="23" """)
      cursor23 = conn.cursor()
      cursor23.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(23,))
      row23 = cursor23.fetchone()
      while row23 is not None:
         if row23[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row23 = cursor23.fetchone()
         else:
            row23 = cursor23.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="24" """)
      cursor24 = conn.cursor()
      cursor24.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(24,))
      row24 = cursor24.fetchone()
      while row24 is not None:
         if row24[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row24 = cursor24.fetchone()
         else:
            row24 = cursor24.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="25" """)
      cursor25 = conn.cursor()
      cursor25.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(25,))
      row25 = cursor25.fetchone()
      while row25 is not None:
         if row25[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row25 = cursor25.fetchone()
         else:
            row25 = cursor25.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="26" """)
      cursor26 = conn.cursor()
      cursor26.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(26,))
      row26 = cursor26.fetchone()
      while row26 is not None:
         if row26[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row26 = cursor26.fetchone()
         else:
            row26 = cursor26.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="27" """)
      cursor27 = conn.cursor()
      cursor27.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(27,))
      row27 = cursor27.fetchone()
      while row27 is not None:
         if row27[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row27 = cursor27.fetchone()
         else:
            row27 = cursor27.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="28" """)
      cursor28 = conn.cursor()
      cursor28.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(28,))
      row28 = cursor28.fetchone()
      while row28 is not None:
         if row28[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row28 = cursor28.fetchone()
         else:
            row28 = cursor28.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="29" """)
      cursor29 = conn.cursor()
      cursor29.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(29,))
      row29 = cursor29.fetchone()
      while row29 is not None:
         if row29[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row29 = cursor29.fetchone()
         else:
            row29 = cursor29.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="30" """)
      cursor30 = conn.cursor()
      cursor30.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(30,))
      row30 = cursor30.fetchone()
      while row30 is not None:
         if row30[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row30 = cursor30.fetchone()
         else:
            row30 = cursor30.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
        </div>

        <div id="col_num">
         <div id="col1_num">
          <p id="spacing">1</p>
         </div>
         <div id="col1_num">
          <p id="spacing">2</p>
         </div>
         <div id="col1_num">
          <p id="spacing">3</p>
         </div>
         <div id="col1_num">
          <p id="spacing">4</p>
         </div>
         <div id="col1_num">
          <p id="spacing">5</p>
         </div>
         <div id="col1_num">
          <p id="spacing">6</p>
         </div>
         <div id="col1_num">
          <p id="spacing">7</p>
         </div>
         <div id="col1_num">
          <p id="spacing">8</p>
         </div>
         <div id="col1_num">
          <p id="spacing">9</p>
         </div>
         <div id="col1_num">
          <p id="spacing_last">10</p>
         </div>

        </div>


        <div id="col">
         <div id="col1">
          <p id="spacing">D E F</p>
         </div>
         <div id="col1">
          <p>
           <a id="31" """)
      cursor31 = conn.cursor()
      cursor31.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(31,))
      row31 = cursor31.fetchone()
      while row31 is not None:
         if row31[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row31 = cursor31.fetchone()
         else:
            row31 = cursor31.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="32" """)
      cursor32 = conn.cursor()
      cursor32.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(32,))
      row32 = cursor32.fetchone()
      while row32 is not None:
         if row32[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row32 = cursor32.fetchone()
         else:
            row32 = cursor32.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="33" """)
      cursor33 = conn.cursor()
      cursor33.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(33,))
      row33 = cursor33.fetchone()
      while row33 is not None:
         if row33[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row33 = cursor33.fetchone()
         else:
            row33 = cursor33.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="34" """)
      cursor34 = conn.cursor()
      cursor34.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(34,))
      row34 = cursor34.fetchone()
      while row34 is not None:
         if row34[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row34 = cursor34.fetchone()
         else:
            row34 = cursor34.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="35" """)
      cursor35 = conn.cursor()
      cursor35.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(35,))
      row35 = cursor35.fetchone()
      while row35 is not None:
         if row35[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row35 = cursor35.fetchone()
         else:
            row35 = cursor35.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="36" """)
      cursor36 = conn.cursor()
      cursor36.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(36,))
      row36 = cursor36.fetchone()
      while row36 is not None:
         if row36[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row36 = cursor36.fetchone()
         else:
            row36 = cursor36.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="37" """)
      cursor37 = conn.cursor()
      cursor37.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(37,))
      row37 = cursor37.fetchone()
      while row37 is not None:
         if row37[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row37 = cursor37.fetchone()
         else:
            row37 = cursor37.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="38" """)
      cursor38 = conn.cursor()
      cursor38.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(38,))
      row38 = cursor38.fetchone()
      while row38 is not None:
         if row38[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row38 = cursor38.fetchone()
         else:
            row38 = cursor38.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="39" """)
      cursor39 = conn.cursor()
      cursor39.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(39,))
      row39 = cursor39.fetchone()
      while row39 is not None:
         if row39[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row39 = cursor39.fetchone()
         else:
            row39 = cursor39.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="40" """)
      cursor40 = conn.cursor()
      cursor40.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(40,))
      row40 = cursor40.fetchone()
      while row40 is not None:
         if row40[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row40 = cursor40.fetchone()
         else:
            row40 = cursor40.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="41" """)
      cursor41 = conn.cursor()
      cursor41.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(41,))
      row41 = cursor41.fetchone()
      while row41 is not None:
         if row41[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row41 = cursor41.fetchone()
         else:
            row41 = cursor41.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="42" """)
      cursor42 = conn.cursor()
      cursor42.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(42,))
      row42 = cursor42.fetchone()
      while row42 is not None:
         if row42[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row42 = cursor42.fetchone()
         else:
            row42 = cursor42.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="43" """)
      cursor43 = conn.cursor()
      cursor43.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(43,))
      row43 = cursor43.fetchone()
      while row43 is not None:
         if row43[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row43 = cursor43.fetchone()
         else:
            row43 = cursor43.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="44" """)
      cursor44 = conn.cursor()
      cursor44.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(44,))
      row44 = cursor44.fetchone()
      while row44 is not None:
         if row44[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row44 = cursor44.fetchone()
         else:
            row44 = cursor44.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="45" """)
      cursor45 = conn.cursor()
      cursor45.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(45,))
      row45 = cursor45.fetchone()
      while row45 is not None:
         if row45[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row45 = cursor45.fetchone()
         else:
            row45 = cursor45.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="46" """)
      cursor46 = conn.cursor()
      cursor46.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(46,))
      row46 = cursor46.fetchone()
      while row46 is not None:
         if row46[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row46 = cursor46.fetchone()
         else:
            row46 = cursor46.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="47" """)
      cursor47 = conn.cursor()
      cursor47.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(47,))
      row47 = cursor47.fetchone()
      while row47 is not None:
         if row47[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row47 = cursor47.fetchone()
         else:
            row47 = cursor47.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="48" """)
      cursor48 = conn.cursor()
      cursor48.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(48,))
      row48 = cursor48.fetchone()
      while row48 is not None:
         if row48[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row48 = cursor48.fetchone()
         else:
            row48 = cursor48.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="49" """)
      cursor49 = conn.cursor()
      cursor49.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(49,))
      row49 = cursor49.fetchone()
      while row49 is not None:
         if row49[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row49 = cursor49.fetchone()
         else:
            row49 = cursor49.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="50" """)
      cursor50 = conn.cursor()
      cursor50.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(50,))
      row50 = cursor50.fetchone()
      while row50 is not None:
         if row50[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row50 = cursor50.fetchone()
         else:
            row50 = cursor50.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="51" """)
      cursor51 = conn.cursor()
      cursor51.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(51,))
      row51 = cursor51.fetchone()
      while row51 is not None:
         if row51[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row51 = cursor51.fetchone()
         else:
            row51 = cursor51.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="52" """)
      cursor52 = conn.cursor()
      cursor52.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(52,))
      row52 = cursor52.fetchone()
      while row52 is not None:
         if row52[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row52 = cursor52.fetchone()
         else:
            row52 = cursor52.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="53" """)
      cursor53 = conn.cursor()
      cursor53.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(53,))
      row53 = cursor53.fetchone()
      while row53 is not None:
         if row53[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row53 = cursor53.fetchone()
         else:
            row53 = cursor53.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="54" """)
      cursor54 = conn.cursor()
      cursor54.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(54,))
      row54 = cursor54.fetchone()
      while row54 is not None:
         if row54[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row54 = cursor54.fetchone()
         else:
            row54 = cursor54.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="55" """)
      cursor55 = conn.cursor()
      cursor55.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(55,))
      row55 = cursor55.fetchone()
      while row55 is not None:
         if row55[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row55 = cursor55.fetchone()
         else:
            row55 = cursor55.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="56" """)
      cursor56 = conn.cursor()
      cursor56.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(56,))
      row56 = cursor56.fetchone()
      while row56 is not None:
         if row56[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row56 = cursor56.fetchone()
         else:
            row56 = cursor56.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="57" """)
      cursor57 = conn.cursor()
      cursor57.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(57,))
      row57 = cursor57.fetchone()
      while row57 is not None:
         if row57[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row57 = cursor57.fetchone()
         else:
            row57 = cursor57.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="58" """)
      cursor58 = conn.cursor()
      cursor58.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(58,))
      row58 = cursor58.fetchone()
      while row58 is not None:
         if row58[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row58 = cursor58.fetchone()
         else:
            row58 = cursor58.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="59" """)
      cursor59 = conn.cursor()
      cursor59.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(59,))
      row59 = cursor59.fetchone()
      while row59 is not None:
         if row59[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row59 = cursor59.fetchone()
         else:
            row59 = cursor59.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="60" """)
      cursor60 = conn.cursor()
      cursor60.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(60,))
      row60 = cursor60.fetchone()
      while row60 is not None:
         if row60[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row60 = cursor60.fetchone()
         else:
            row60 = cursor60.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
        </div>
       </div>""")
   else:               ############################################
      end_date=form.getvalue('end_date')
      st_date2 = datetime.datetime.strptime(end_date, ' %m/%d/%Y ')
      fromdate2 = date(now.year,now.month,now.day)
      todate2 = date(st_date2.year,st_date2.month,st_date2.day)
      daygenerator2 = (fromdate2 + timedelta(x + 1) for x in range((todate2 - fromdate2).days))
      days_from_today2=sum(1 for day in daygenerator2 if day.weekday() > 0)
      days_dif2 = days_from_today2
      leave2=form.getvalue('leave2')
      flight_time2=form.getvalue('flight_time2')
      arrive2=form.getvalue('arrive2')
      fare2=form.getvalue('fare2')
      l2=leave2.strip()
      coll2=str(end_dest+"-"+start_dest+"- "+l2).strip()
      dest2=str(end_dest+"-"+start_dest).strip()

      print("""
				<div id="empty-div" style="opacity:0">""</div>
				<H2 style="margin-left:20px;">Journey</H2>
	  			<div id="results-offer">
					<div id="results-offer-select">
						<p style='font-size:33px;'>&#163;""",fare,"""</p>
					</div>
					<div style="border-bottom:1px solid #636363;" id="results-depart">
						<p style="font-size:20px;color:red;">Depart</p><p style="font-size:18px;">""",start_dest,'-',end_dest,"""</p><p style='font-size:17px;'>""",start_date,"""</p> <br><br>
						<table id="table-size">
						  <tr>
							<th align="left">Leave</th>
							<th align="center">Journey Time</th>
							<th align="right">Arrive</th>
						  </tr>
						  <tr>
							<td align="left">""",leave1,"""</td>
							<td align="center">""",flight_time1,"""</td>
							<td align="right">""",arrive1,"""</td>
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
							<td align="left">""",leave2,"""</td>
							<td align="center">""",flight_time2,"""</td>
							<td align="right">""",arrive2,"""</td>
						  </tr>
						</table>
					</div>
				</div>
    <input id='seatmincheck' name='seatmincheck' style="position:absolute;margin-top:100px;margin-left:-45px;z-index:-900;opacity:0;" required/>
				<H2 style="margin-top:100px;margin-left:20px;">Choose your seats for Departing</H2>
				<div id="col_legend1" style="margin-left:20px;">
						<div id="col1">
							<p id="spacing_last">Legend</p>
						</div>
						<div id="col_legend">
							<p>
								<a class="button_seats button_green button_about" style="pointer-events: none;"></a
							</p>
						</div>
						<div id="col_legend">
							<p>
								<a class="button_seats button_green button_about" style="pointer-events: none;background-color:red;"></a>
							</p>
						</div>
						<div id="col_legend">
							<p>
								<a class="button_seats button_green button_about" style="pointer-events: none;background-color:orange;"></a>
							</p>
						</div>
				</div>
				<div id="col_num">
						<div id="col1_lt" style="margin-top:45px">
							<p id="spacing_last">Seat is free</p>
						</div>
						<div id="col1_lt">
							<p id="spacing_last">Seat is occupied</p>
						</div>
						<div id="col1_lt">
							<p id="spacing_last">Selected seat</p>
						</div>
					</div>
				<div id="seats">
					<div id="col">
						<div id="col1">
							<p id="spacing">A B C</p>
						</div>
						<div id="col1">
							<p>
								<a id="1" """)
      cursor1 = conn.cursor()
      cursor1.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(1,))
      row1 = cursor1.fetchone()
      while row1 is not None:
         if row1[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row1 = cursor1.fetchone()
         else:
            row1 = cursor1.fetchone()
         print("""
         class="button_seats button_green button_about"></a>
								<a id="2" """)
      cursor2 = conn.cursor()
      cursor2.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(2,))
      row2 = cursor2.fetchone()
      while row2 is not None:
         if row2[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row2 = cursor2.fetchone()
         else:
            row2 = cursor2.fetchone()
         print("""class="button_seats button_green button_about"></a>
								<a id="3" """)
      cursor3 = conn.cursor()
      cursor3.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(3,))
      row3 = cursor3.fetchone()
      while row3 is not None:
         if row3[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row3 = cursor3.fetchone()
         else:
            row3 = cursor3.fetchone()
         print("""class="button_seats button_green button_about"></a>
							</p>
						</div>
						<div id="col1">
							<p>
								<a id="4" """)
      cursor4 = conn.cursor()
      cursor4.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(4,))
      row4 = cursor4.fetchone()
      while row4 is not None:
         if row4[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row4 = cursor4.fetchone()
         else:
            row4 = cursor4.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="5" """)
      cursor5 = conn.cursor()
      cursor5.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(5,))
      row5 = cursor5.fetchone()
      while row5 is not None:
         if row5[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row5 = cursor5.fetchone()
         else:
            row5 = cursor5.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="6" """)
      cursor6 = conn.cursor()
      cursor6.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(6,))
      row6 = cursor6.fetchone()
      while row6 is not None:
         if row6[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row6 = cursor6.fetchone()
         else:
            row6 = cursor6.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="7" """)
      cursor7 = conn.cursor()
      cursor7.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(7,))
      row7 = cursor7.fetchone()
      while row7 is not None:
         if row7[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row7 = cursor7.fetchone()
         else:
            row7 = cursor7.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="8" """)
      cursor8 = conn.cursor()
      cursor8.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(8,))
      row8 = cursor8.fetchone()
      while row8 is not None:
         if row8[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row8 = cursor8.fetchone()
         else:
            row8 = cursor8.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="9" """)
      cursor9 = conn.cursor()
      cursor9.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(9,))
      row9 = cursor9.fetchone()
      while row9 is not None:
         if row9[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row9 = cursor9.fetchone()
         else:
            row9 = cursor9.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="10" """)
      cursor10 = conn.cursor()
      cursor10.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(10,))
      row10 = cursor10.fetchone()
      while row10 is not None:
         if row10[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row10 = cursor10.fetchone()
         else:
            row10 = cursor10.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="11" """)
      cursor11 = conn.cursor()
      cursor11.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(11,))
      row11 = cursor11.fetchone()
      while row11 is not None:
         if row11[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row11 = cursor11.fetchone()
         else:
            row11 = cursor11.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="12" """)
      cursor12 = conn.cursor()
      cursor12.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(12,))
      row12 = cursor12.fetchone()
      while row12 is not None:
         if row12[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row12 = cursor12.fetchone()
         else:
            row12 = cursor12.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="13" """)
      cursor13 = conn.cursor()
      cursor13.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(13,))
      row13 = cursor13.fetchone()
      while row13 is not None:
         if row13[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row13 = cursor13.fetchone()
         else:
            row13 = cursor13.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="14" """)
      cursor14 = conn.cursor()
      cursor14.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(14,))
      row14 = cursor14.fetchone()
      while row14 is not None:
         if row14[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row14 = cursor14.fetchone()
         else:
            row14 = cursor14.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="15" """)
      cursor15 = conn.cursor()
      cursor15.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(15,))
      row15 = cursor15.fetchone()
      while row15 is not None:
         if row15[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row15 = cursor15.fetchone()
         else:
            row15 = cursor15.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="16" """)
      cursor16 = conn.cursor()
      cursor16.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(16,))
      row16 = cursor16.fetchone()
      while row16 is not None:
         if row16[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row16 = cursor16.fetchone()
         else:
            row16 = cursor16.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="17" """)
      cursor17 = conn.cursor()
      cursor17.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(17,))
      row17 = cursor17.fetchone()
      while row17 is not None:
         if row17[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row17 = cursor17.fetchone()
         else:
            row17 = cursor17.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="18" """)
      cursor18 = conn.cursor()
      cursor18.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(18,))
      row18 = cursor18.fetchone()
      while row18 is not None:
         if row18[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row18 = cursor18.fetchone()
         else:
            row18 = cursor18.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="19" """)
      cursor19 = conn.cursor()
      cursor19.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(19,))
      row19 = cursor19.fetchone()
      while row19 is not None:
         if row19[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row19 = cursor19.fetchone()
         else:
            row19 = cursor19.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="20" """)
      cursor20 = conn.cursor()
      cursor20.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(20,))
      row20 = cursor20.fetchone()
      while row20 is not None:
         if row20[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row20 = cursor20.fetchone()
         else:
            row20 = cursor20.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="21" """)
      cursor21 = conn.cursor()
      cursor21.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(21,))
      row21 = cursor21.fetchone()
      while row21 is not None:
         if row21[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row21 = cursor21.fetchone()
         else:
            row21 = cursor21.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="22" """)
      cursor22 = conn.cursor()
      cursor22.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(22,))
      row22 = cursor22.fetchone()
      while row22 is not None:
         if row22[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row22 = cursor22.fetchone()
         else:
            row22 = cursor22.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="23" """)
      cursor23 = conn.cursor()
      cursor23.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(23,))
      row23 = cursor23.fetchone()
      while row23 is not None:
         if row23[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row23 = cursor23.fetchone()
         else:
            row23 = cursor23.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="24" """)
      cursor24 = conn.cursor()
      cursor24.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(24,))
      row24 = cursor24.fetchone()
      while row24 is not None:
         if row24[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row24 = cursor24.fetchone()
         else:
            row24 = cursor24.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="25" """)
      cursor25 = conn.cursor()
      cursor25.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(25,))
      row25 = cursor25.fetchone()
      while row25 is not None:
         if row25[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row25 = cursor25.fetchone()
         else:
            row25 = cursor25.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="26" """)
      cursor26 = conn.cursor()
      cursor26.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(26,))
      row26 = cursor26.fetchone()
      while row26 is not None:
         if row26[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row26 = cursor26.fetchone()
         else:
            row26 = cursor26.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="27" """)
      cursor27 = conn.cursor()
      cursor27.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(27,))
      row27 = cursor27.fetchone()
      while row27 is not None:
         if row27[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row27 = cursor27.fetchone()
         else:
            row27 = cursor27.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="28" """)
      cursor28 = conn.cursor()
      cursor28.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(28,))
      row28 = cursor28.fetchone()
      while row28 is not None:
         if row28[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row28 = cursor28.fetchone()
         else:
            row28 = cursor28.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="29" """)
      cursor29 = conn.cursor()
      cursor29.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(29,))
      row29 = cursor29.fetchone()
      while row29 is not None:
         if row29[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row29 = cursor29.fetchone()
         else:
            row29 = cursor29.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="30" """)
      cursor30 = conn.cursor()
      cursor30.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(30,))
      row30 = cursor30.fetchone()
      while row30 is not None:
         if row30[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row30 = cursor30.fetchone()
         else:
            row30 = cursor30.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
        </div>

        <div id="col_num">
         <div id="col1_num">
          <p id="spacing">1</p>
         </div>
         <div id="col1_num">
          <p id="spacing">2</p>
         </div>
         <div id="col1_num">
          <p id="spacing">3</p>
         </div>
         <div id="col1_num">
          <p id="spacing">4</p>
         </div>
         <div id="col1_num">
          <p id="spacing">5</p>
         </div>
         <div id="col1_num">
          <p id="spacing">6</p>
         </div>
         <div id="col1_num">
          <p id="spacing">7</p>
         </div>
         <div id="col1_num">
          <p id="spacing">8</p>
         </div>
         <div id="col1_num">
          <p id="spacing">9</p>
         </div>
         <div id="col1_num">
          <p id="spacing_last">10</p>
         </div>

        </div>


        <div id="col">
         <div id="col1">
          <p id="spacing">D E F</p>
         </div>
         <div id="col1">
          <p>
           <a id="31" """)
      cursor31 = conn.cursor()
      cursor31.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(31,))
      row31 = cursor31.fetchone()
      while row31 is not None:
         if row31[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row31 = cursor31.fetchone()
         else:
            row31 = cursor31.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="32" """)
      cursor32 = conn.cursor()
      cursor32.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(32,))
      row32 = cursor32.fetchone()
      while row32 is not None:
         if row32[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row32 = cursor32.fetchone()
         else:
            row32 = cursor32.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="33" """)
      cursor33 = conn.cursor()
      cursor33.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(33,))
      row33 = cursor33.fetchone()
      while row33 is not None:
         if row33[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row33 = cursor33.fetchone()
         else:
            row33 = cursor33.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="34" """)
      cursor34 = conn.cursor()
      cursor34.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(34,))
      row34 = cursor34.fetchone()
      while row34 is not None:
         if row34[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row34 = cursor34.fetchone()
         else:
            row34 = cursor34.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="35" """)
      cursor35 = conn.cursor()
      cursor35.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(35,))
      row35 = cursor35.fetchone()
      while row35 is not None:
         if row35[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row35 = cursor35.fetchone()
         else:
            row35 = cursor35.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="36" """)
      cursor36 = conn.cursor()
      cursor36.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(36,))
      row36 = cursor36.fetchone()
      while row36 is not None:
         if row36[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row36 = cursor36.fetchone()
         else:
            row36 = cursor36.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="37" """)
      cursor37 = conn.cursor()
      cursor37.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(37,))
      row37 = cursor37.fetchone()
      while row37 is not None:
         if row37[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row37 = cursor37.fetchone()
         else:
            row37 = cursor37.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="38" """)
      cursor38 = conn.cursor()
      cursor38.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(38,))
      row38 = cursor38.fetchone()
      while row38 is not None:
         if row38[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row38 = cursor38.fetchone()
         else:
            row38 = cursor38.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="39" """)
      cursor39 = conn.cursor()
      cursor39.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(39,))
      row39 = cursor39.fetchone()
      while row39 is not None:
         if row39[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row39 = cursor39.fetchone()
         else:
            row39 = cursor39.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="40" """)
      cursor40 = conn.cursor()
      cursor40.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(40,))
      row40 = cursor40.fetchone()
      while row40 is not None:
         if row40[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row40 = cursor40.fetchone()
         else:
            row40 = cursor40.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="41" """)
      cursor41 = conn.cursor()
      cursor41.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(41,))
      row41 = cursor41.fetchone()
      while row41 is not None:
         if row41[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row41 = cursor41.fetchone()
         else:
            row41 = cursor41.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="42" """)
      cursor42 = conn.cursor()
      cursor42.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(42,))
      row42 = cursor42.fetchone()
      while row42 is not None:
         if row42[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row42 = cursor42.fetchone()
         else:
            row42 = cursor42.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="43" """)
      cursor43 = conn.cursor()
      cursor43.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(43,))
      row43 = cursor43.fetchone()
      while row43 is not None:
         if row43[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row43 = cursor43.fetchone()
         else:
            row43 = cursor43.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="44" """)
      cursor44 = conn.cursor()
      cursor44.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(44,))
      row44 = cursor44.fetchone()
      while row44 is not None:
         if row44[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row44 = cursor44.fetchone()
         else:
            row44 = cursor44.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="45" """)
      cursor45 = conn.cursor()
      cursor45.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(45,))
      row45 = cursor45.fetchone()
      while row45 is not None:
         if row45[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row45 = cursor45.fetchone()
         else:
            row45 = cursor45.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="46" """)
      cursor46 = conn.cursor()
      cursor46.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(46,))
      row46 = cursor46.fetchone()
      while row46 is not None:
         if row46[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row46 = cursor46.fetchone()
         else:
            row46 = cursor46.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="47" """)
      cursor47 = conn.cursor()
      cursor47.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(47,))
      row47 = cursor47.fetchone()
      while row47 is not None:
         if row47[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row47 = cursor47.fetchone()
         else:
            row47 = cursor47.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="48" """)
      cursor48 = conn.cursor()
      cursor48.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(48,))
      row48 = cursor48.fetchone()
      while row48 is not None:
         if row48[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row48 = cursor48.fetchone()
         else:
            row48 = cursor48.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="49" """)
      cursor49 = conn.cursor()
      cursor49.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(49,))
      row49 = cursor49.fetchone()
      while row49 is not None:
         if row49[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row49 = cursor49.fetchone()
         else:
            row49 = cursor49.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="50" """)
      cursor50 = conn.cursor()
      cursor50.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(50,))
      row50 = cursor50.fetchone()
      while row50 is not None:
         if row50[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row50 = cursor50.fetchone()
         else:
            row50 = cursor50.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="51" """)
      cursor51 = conn.cursor()
      cursor51.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(51,))
      row51 = cursor51.fetchone()
      while row51 is not None:
         if row51[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row51 = cursor51.fetchone()
         else:
            row51 = cursor51.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="52" """)
      cursor52 = conn.cursor()
      cursor52.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(52,))
      row52 = cursor52.fetchone()
      while row52 is not None:
         if row52[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row52 = cursor52.fetchone()
         else:
            row52 = cursor52.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="53" """)
      cursor53 = conn.cursor()
      cursor53.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(53,))
      row53 = cursor53.fetchone()
      while row53 is not None:
         if row53[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row53 = cursor53.fetchone()
         else:
            row53 = cursor53.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="54" """)
      cursor54 = conn.cursor()
      cursor54.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(54,))
      row54 = cursor54.fetchone()
      while row54 is not None:
         if row54[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row54 = cursor54.fetchone()
         else:
            row54 = cursor54.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="55" """)
      cursor55 = conn.cursor()
      cursor55.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(55,))
      row55 = cursor55.fetchone()
      while row55 is not None:
         if row55[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row55 = cursor55.fetchone()
         else:
            row55 = cursor55.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="56" """)
      cursor56 = conn.cursor()
      cursor56.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(56,))
      row56 = cursor56.fetchone()
      while row56 is not None:
         if row56[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row56 = cursor56.fetchone()
         else:
            row56 = cursor56.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="57" """)
      cursor57 = conn.cursor()
      cursor57.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(57,))
      row57 = cursor57.fetchone()
      while row57 is not None:
         if row57[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row57 = cursor57.fetchone()
         else:
            row57 = cursor57.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="58" """)
      cursor58 = conn.cursor()
      cursor58.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(58,))
      row58 = cursor58.fetchone()
      while row58 is not None:
         if row58[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row58 = cursor58.fetchone()
         else:
            row58 = cursor58.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="59" """)
      cursor59 = conn.cursor()
      cursor59.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(59,))
      row59 = cursor59.fetchone()
      while row59 is not None:
         if row59[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row59 = cursor59.fetchone()
         else:
            row59 = cursor59.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="60" """)
      cursor60 = conn.cursor()
      cursor60.execute("SELECT * FROM `"+coll1+"` WHERE seat_id = %s" ,(60,))
      row60 = cursor60.fetchone()
      while row60 is not None:
         if row60[days_from_today+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row60 = cursor60.fetchone()
         else:
            row60 = cursor60.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
        </div>
       </div>
       <input id='seatmincheck1' name='seatmincheck1' style="position:absolute;margin-top:100px;margin-left:-45px;z-index:-900;opacity:0;" required/>
       <H2 style="margin-top:100px;margin-left:20px;">Choose your seats for Returning</H2>
				<div id="col_legend1" style="margin-left:20px;">
						<div id="col1">
							<p id="spacing_last">Legend</p>
						</div>
						<div id="col_legend">
							<p>
								<a class="button_seats button_green button_about" style="pointer-events: none;"></a
							</p>
						</div>
						<div id="col_legend">
							<p>
								<a class="button_seats button_green button_about" style="pointer-events: none;background-color:red;"></a>
							</p>
						</div>
						<div id="col_legend">
							<p>
								<a class="button_seats button_green button_about" style="pointer-events: none;background-color:orange;"></a>
							</p>
						</div>
				</div>
				<div id="col_num">
						<div id="col1_lt" style="margin-top:45px">
							<p id="spacing_last">Seat is free</p>
						</div>
						<div id="col1_lt">
							<p id="spacing_last">Seat is occupied</p>
						</div>
						<div id="col1_lt">
							<p id="spacing_last">Selected seat</p>
						</div>
					</div>
				<div id="seats">
					<div id="col">
						<div id="col1">
							<p id="spacing">A B C</p>
						</div>
						<div id="col1">
							<p>
								<a id="61" """)
      cursor61 = conn.cursor()
      cursor61.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(1,))
      row61 = cursor61.fetchone()
      while row61 is not None:
         if row61[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row61 = cursor61.fetchone()
         else:
            row61 = cursor61.fetchone()
         print("""
         class="button_seats button_green button_about"></a>
								<a id="62" """)
      cursor62 = conn.cursor()
      cursor62.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(2,))
      row62 = cursor62.fetchone()
      while row62 is not None:
         if row62[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row62 = cursor62.fetchone()
         else:
            row62 = cursor62.fetchone()
         print("""class="button_seats button_green button_about"></a>
								<a id="63" """)
      cursor63 = conn.cursor()
      cursor63.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(3,))
      row63 = cursor63.fetchone()
      while row63 is not None:
         if row63[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row63 = cursor63.fetchone()
         else:
            row63 = cursor63.fetchone()
         print("""class="button_seats button_green button_about"></a>
							</p>
						</div>
						<div id="col1">
							<p>
								<a id="64" """)
      cursor64 = conn.cursor()
      cursor64.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(4,))
      row64 = cursor64.fetchone()
      while row64 is not None:
         if row64[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row64 = cursor64.fetchone()
         else:
            row64 = cursor64.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="65" """)
      cursor65 = conn.cursor()
      cursor65.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(5,))
      row65 = cursor65.fetchone()
      while row65 is not None:
         if row65[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row65 = cursor65.fetchone()
         else:
            row65 = cursor65.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="66" """)
      cursor66 = conn.cursor()
      cursor66.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(6,))
      row66 = cursor66.fetchone()
      while row66 is not None:
         if row66[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row66 = cursor66.fetchone()
         else:
            row66 = cursor66.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="67" """)
      cursor67 = conn.cursor()
      cursor67.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(7,))
      row67 = cursor67.fetchone()
      while row67 is not None:
         if row67[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row67 = cursor67.fetchone()
         else:
            row67 = cursor67.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="68" """)
      cursor68 = conn.cursor()
      cursor68.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(8,))
      row68 = cursor68.fetchone()
      while row68 is not None:
         if row68[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row68 = cursor68.fetchone()
         else:
            row68 = cursor68.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="69" """)
      cursor69 = conn.cursor()
      cursor69.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(9,))
      row69 = cursor69.fetchone()
      while row69 is not None:
         if row69[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row69 = cursor69.fetchone()
         else:
            row69 = cursor69.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="70" """)
      cursor70 = conn.cursor()
      cursor70.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(10,))
      row70 = cursor70.fetchone()
      while row70 is not None:
         if row70[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row70 = cursor70.fetchone()
         else:
            row70 = cursor70.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="71" """)
      cursor71 = conn.cursor()
      cursor71.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(11,))
      row71 = cursor71.fetchone()
      while row71 is not None:
         if row71[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row71 = cursor71.fetchone()
         else:
            row71 = cursor71.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="72" """)
      cursor72 = conn.cursor()
      cursor72.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(12,))
      row72 = cursor72.fetchone()
      while row72 is not None:
         if row72[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row72 = cursor72.fetchone()
         else:
            row72 = cursor72.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="73" """)
      cursor73 = conn.cursor()
      cursor73.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(13,))
      row73 = cursor73.fetchone()
      while row73 is not None:
         if row73[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row73 = cursor73.fetchone()
         else:
            row73 = cursor73.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="74" """)
      cursor74 = conn.cursor()
      cursor74.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(14,))
      row74 = cursor74.fetchone()
      while row74 is not None:
         if row74[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row74 = cursor74.fetchone()
         else:
            row74 = cursor74.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="75" """)
      cursor75 = conn.cursor()
      cursor75.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(15,))
      row75 = cursor75.fetchone()
      while row75 is not None:
         if row75[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row75 = cursor75.fetchone()
         else:
            row75 = cursor75.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="76" """)
      cursor76 = conn.cursor()
      cursor76.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(16,))
      row76 = cursor76.fetchone()
      while row76 is not None:
         if row76[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row76 = cursor76.fetchone()
         else:
            row76 = cursor76.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="77" """)
      cursor77 = conn.cursor()
      cursor77.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(17,))
      row77 = cursor77.fetchone()
      while row77 is not None:
         if row77[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row77 = cursor77.fetchone()
         else:
            row77 = cursor77.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="78" """)
      cursor78 = conn.cursor()
      cursor78.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(18,))
      row78 = cursor78.fetchone()
      while row78 is not None:
         if row78[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row78 = cursor78.fetchone()
         else:
            row78 = cursor78.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="79" """)
      cursor79 = conn.cursor()
      cursor79.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(19,))
      row79 = cursor79.fetchone()
      while row79 is not None:
         if row79[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row79 = cursor79.fetchone()
         else:
            row79 = cursor79.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="80" """)
      cursor80 = conn.cursor()
      cursor80.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(20,))
      row80 = cursor80.fetchone()
      while row80 is not None:
         if row80[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row80 = cursor80.fetchone()
         else:
            row80 = cursor80.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="81" """)
      cursor81 = conn.cursor()
      cursor81.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(21,))
      row81 = cursor81.fetchone()
      while row81 is not None:
         if row81[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row81 = cursor81.fetchone()
         else:
            row81 = cursor81.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="82" """)
      cursor82 = conn.cursor()
      cursor82.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(22,))
      row82 = cursor82.fetchone()
      while row82 is not None:
         if row82[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row82 = cursor82.fetchone()
         else:
            row82 = cursor82.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="83" """)
      cursor83 = conn.cursor()
      cursor83.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(23,))
      row83 = cursor83.fetchone()
      while row83 is not None:
         if row83[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row83 = cursor83.fetchone()
         else:
            row83 = cursor83.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="84" """)
      cursor84 = conn.cursor()
      cursor84.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(24,))
      row84 = cursor84.fetchone()
      while row84 is not None:
         if row84[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row84 = cursor84.fetchone()
         else:
            row84 = cursor84.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="85" """)
      cursor85 = conn.cursor()
      cursor85.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(25,))
      row85 = cursor85.fetchone()
      while row85 is not None:
         if row85[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row85 = cursor85.fetchone()
         else:
            row85 = cursor85.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="86" """)
      cursor86 = conn.cursor()
      cursor86.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(26,))
      row86 = cursor86.fetchone()
      while row86 is not None:
         if row86[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row86 = cursor86.fetchone()
         else:
            row86 = cursor86.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="87" """)
      cursor87 = conn.cursor()
      cursor87.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(27,))
      row87 = cursor87.fetchone()
      while row87 is not None:
         if row87[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row87 = cursor87.fetchone()
         else:
            row87 = cursor87.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="88" """)
      cursor88 = conn.cursor()
      cursor88.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(28,))
      row88 = cursor88.fetchone()
      while row88 is not None:
         if row88[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row88 = cursor88.fetchone()
         else:
            row88 = cursor88.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="89" """)
      cursor89 = conn.cursor()
      cursor89.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(29,))
      row89 = cursor89.fetchone()
      while row89 is not None:
         if row89[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row89 = cursor89.fetchone()
         else:
            row89 = cursor89.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="90" """)
      cursor90 = conn.cursor()
      cursor90.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(30,))
      row90 = cursor90.fetchone()
      while row90 is not None:
         if row90[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row90 = cursor90.fetchone()
         else:
            row90 = cursor90.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
        </div>

        <div id="col_num">
         <div id="col1_num">
          <p id="spacing">1</p>
         </div>
         <div id="col1_num">
          <p id="spacing">2</p>
         </div>
         <div id="col1_num">
          <p id="spacing">3</p>
         </div>
         <div id="col1_num">
          <p id="spacing">4</p>
         </div>
         <div id="col1_num">
          <p id="spacing">5</p>
         </div>
         <div id="col1_num">
          <p id="spacing">6</p>
         </div>
         <div id="col1_num">
          <p id="spacing">7</p>
         </div>
         <div id="col1_num">
          <p id="spacing">8</p>
         </div>
         <div id="col1_num">
          <p id="spacing">9</p>
         </div>
         <div id="col1_num">
          <p id="spacing_last">10</p>
         </div>

        </div>


        <div id="col">
         <div id="col1">
          <p id="spacing">D E F</p>
         </div>
         <div id="col1">
          <p>
           <a id="91" """)
      cursor91 = conn.cursor()
      cursor91.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(31,))
      row91 = cursor91.fetchone()
      while row91 is not None:
         if row91[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row91 = cursor91.fetchone()
         else:
            row91 = cursor91.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="92" """)
      cursor92 = conn.cursor()
      cursor92.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(32,))
      row92 = cursor92.fetchone()
      while row92 is not None:
         if row92[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row92 = cursor92.fetchone()
         else:
            row92 = cursor92.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="93" """)
      cursor93 = conn.cursor()
      cursor93.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(33,))
      row93 = cursor93.fetchone()
      while row93 is not None:
         if row93[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row93 = cursor93.fetchone()
         else:
            row93 = cursor93.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="94" """)
      cursor94 = conn.cursor()
      cursor94.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(34,))
      row94 = cursor94.fetchone()
      while row94 is not None:
         if row94[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row94 = cursor94.fetchone()
         else:
            row94 = cursor94.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="95" """)
      cursor95 = conn.cursor()
      cursor95.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(35,))
      row95 = cursor95.fetchone()
      while row95 is not None:
         if row95[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row95 = cursor95.fetchone()
         else:
            row95 = cursor95.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="96" """)
      cursor96 = conn.cursor()
      cursor96.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(36,))
      row96 = cursor96.fetchone()
      while row96 is not None:
         if row96[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row96 = cursor96.fetchone()
         else:
            row96 = cursor96.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="97" """)
      cursor97 = conn.cursor()
      cursor97.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(37,))
      row97 = cursor97.fetchone()
      while row97 is not None:
         if row97[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row97 = cursor97.fetchone()
         else:
            row97 = cursor97.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="98" """)
      cursor98 = conn.cursor()
      cursor98.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(38,))
      row98 = cursor98.fetchone()
      while row98 is not None:
         if row98[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row98 = cursor98.fetchone()
         else:
            row98 = cursor98.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="99" """)
      cursor99 = conn.cursor()
      cursor99.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(39,))
      row99 = cursor99.fetchone()
      while row99 is not None:
         if row99[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row99 = cursor99.fetchone()
         else:
            row99 = cursor99.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="100" """)
      cursor100 = conn.cursor()
      cursor100.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(40,))
      row100 = cursor100.fetchone()
      while row100 is not None:
         if row100[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row100 = cursor100.fetchone()
         else:
            row100 = cursor100.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="101" """)
      cursor101 = conn.cursor()
      cursor101.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(41,))
      row101 = cursor101.fetchone()
      while row101 is not None:
         if row101[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row101 = cursor101.fetchone()
         else:
            row101 = cursor101.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="102" """)
      cursor102 = conn.cursor()
      cursor102.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(42,))
      row102 = cursor102.fetchone()
      while row102 is not None:
         if row102[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row102 = cursor102.fetchone()
         else:
            row102 = cursor102.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="103" """)
      cursor103 = conn.cursor()
      cursor103.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(43,))
      row103 = cursor103.fetchone()
      while row103 is not None:
         if row103[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row103 = cursor103.fetchone()
         else:
            row103 = cursor103.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="104" """)
      cursor104 = conn.cursor()
      cursor104.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(44,))
      row104 = cursor104.fetchone()
      while row104 is not None:
         if row104[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row104 = cursor104.fetchone()
         else:
            row104 = cursor104.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="105" """)
      cursor105 = conn.cursor()
      cursor105.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(45,))
      row105 = cursor105.fetchone()
      while row105 is not None:
         if row105[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row105 = cursor105.fetchone()
         else:
            row105 = cursor105.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="106" """)
      cursor106 = conn.cursor()
      cursor106.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(46,))
      row106 = cursor106.fetchone()
      while row106 is not None:
         if row106[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row106 = cursor106.fetchone()
         else:
            row106 = cursor106.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="107" """)
      cursor107 = conn.cursor()
      cursor107.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(47,))
      row107 = cursor107.fetchone()
      while row107 is not None:
         if row107[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row107 = cursor107.fetchone()
         else:
            row107 = cursor107.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="108" """)
      cursor108 = conn.cursor()
      cursor108.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(48,))
      row108 = cursor108.fetchone()
      while row108 is not None:
         if row108[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row108 = cursor108.fetchone()
         else:
            row108 = cursor108.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="109" """)
      cursor109 = conn.cursor()
      cursor109.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(49,))
      row109 = cursor109.fetchone()
      while row109 is not None:
         if row109[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row109 = cursor109.fetchone()
         else:
            row109 = cursor109.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="110" """)
      cursor110 = conn.cursor()
      cursor110.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(50,))
      row110 = cursor110.fetchone()
      while row110 is not None:
         if row110[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row110 = cursor110.fetchone()
         else:
            row110 = cursor110.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="111" """)
      cursor111 = conn.cursor()
      cursor111.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(51,))
      row111 = cursor111.fetchone()
      while row111 is not None:
         if row111[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row111 = cursor111.fetchone()
         else:
            row111 = cursor111.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="112" """)
      cursor112 = conn.cursor()
      cursor112.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(52,))
      row112 = cursor112.fetchone()
      while row112 is not None:
         if row112[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row112 = cursor112.fetchone()
         else:
            row112 = cursor112.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="113" """)
      cursor113 = conn.cursor()
      cursor113.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(53,))
      row113 = cursor113.fetchone()
      while row113 is not None:
         if row113[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row113 = cursor113.fetchone()
         else:
            row113 = cursor113.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="114" """)
      cursor114 = conn.cursor()
      cursor114.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(54,))
      row114 = cursor114.fetchone()
      while row114 is not None:
         if row114[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row114 = cursor114.fetchone()
         else:
            row114 = cursor114.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="115" """)
      cursor115 = conn.cursor()
      cursor115.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(55,))
      row115 = cursor115.fetchone()
      while row115 is not None:
         if row115[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row115 = cursor115.fetchone()
         else:
            row115 = cursor115.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="116" """)
      cursor116 = conn.cursor()
      cursor116.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(56,))
      row116 = cursor116.fetchone()
      while row116 is not None:
         if row116[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row116 = cursor116.fetchone()
         else:
            row116 = cursor116.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="117" """)
      cursor117 = conn.cursor()
      cursor117.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(57,))
      row117 = cursor117.fetchone()
      while row117 is not None:
         if row117[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row117 = cursor117.fetchone()
         else:
            row117 = cursor117.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
         <div id="col1">
          <p>
           <a id="118" """)
      cursor118 = conn.cursor()
      cursor118.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(58,))
      row118 = cursor118.fetchone()
      while row118 is not None:
         if row118[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row118 = cursor118.fetchone()
         else:
            row118 = cursor118.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="119" """)
      cursor119 = conn.cursor()
      cursor119.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(59,))
      row119 = cursor119.fetchone()
      while row119 is not None:
         if row119[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row119 = cursor119.fetchone()
         else:
            row119 = cursor119.fetchone()
         print("""class="button_seats button_green button_about"></a>
           <a id="120" """)
      cursor120 = conn.cursor()
      cursor120.execute("SELECT * FROM `"+coll2+"` WHERE seat_id = %s" ,(60,))
      row120 = cursor120.fetchone()
      while row120 is not None:
         if row120[days_from_today2+1] == 0:
            print(""" style="pointer-events: none;background-color:red;" """)
            row120 = cursor120.fetchone()
         else:
            row120 = cursor120.fetchone()
         print("""class="button_seats button_green button_about"></a>
          </p>
         </div>
        </div>
       </div>""") 
   print("""

      <H2 style="margin-top:100px;margin-left:20px;">Enter passangers details</H2>""")
   for adlts_ in range(1,int(adl)+1):
      print("""
      
      
      <table style="width:100%;">
        <tr>
          <td>
            <H3 style="margin-bottom:0px;margin-left:50px;font-size:17px;">Adult """,adlts_ ,"""</H2>
          </td>
        </tr>
        <tr>
          <td style="width:20%;">
            <H3 style="margin-top:10px;margin-left:80px;font-size:14px;">Name: </H3>
          </td>
          <td><input name='name1""",adlts_,"""' id='name1""",adlts_,"""' onchange="nameinarr1(""",adlts_,""");" class='name' type="text"  placeholder= "by ID"  required/></td>
        </tr>
        <tr>
          <td style="width:20%;">
            <H3 style="margin-top:10px;margin-left:80px;font-size:14px;">Surname: </H3>
          </td>
          <td><input name='surname1""",adlts_,"""' id='surname1""",adlts_,"""' onchange="nameinarr1(""",adlts_,""");" class='name' type="text" placeholder= "by ID"  required/></td>
        </tr>
        <tr>
          <td style="width:20%;">
            <H3 style="margin-top:10px;margin-left:80px;font-size:14px;">Gender: </H3>
          </td>
          <td style="width:50%;">
            <div style="float: left; width: 80px;" class="styled-select">
               <select id="gender" required>
                  <option value="" disabled selected>Select</option>
                  <option>Male</option>
                  <option>Female</option>
               </select>
            </div>
          </td>
          <td></td>
        </tr>
        <tr>
          <td style="width:20%;border:">
            <H3 style="margin-top:10px;margin-left:80px;font-size:14px;">Date of birth: </H3>
          </td>
          <td style="width:20%;">
            <div  style="float: left; width: 66px;" class="styled-select">
               <select name='day1""",adlts_,"""' required>
                  <option value="" disabled selected>Day</option>""")
      for num_days in range(1,32):
         print("""<option value='""",num_days,"""'>""",num_days,"""</option>""")
      print("""
               </select>
            </div>
            <div  style="float: left; width: 66px;" class="styled-select">
               <select name='month1""",adlts_,"""' onchange="calladl('day1""",adlts_,"""','month1""",adlts_,"""','year1""",adlts_,"""')" required>
                  <option value="" disabled selected>Month</option>
                     <option value="1">Jan</option> 
                     <option value="2">Feb</option> 
                     <option value="3">Mar</option> 
                     <option value="4">Apr</option> 
                     <option value="5">May</option> 
                     <option value="6">Jun</option> 
                     <option value="7">Jul</option> 
                     <option value="8">Aug</option> 
                     <option value="9">Sep</option> 
                     <option value="10">Oct</option> 
                     <option value="11">Nov</option> 
                     <option value="12">Dec</option> 
               </select>
            </div>
            <div  style="float: left; width: 66px;" class="styled-select">
               <select name='year1""",adlts_,"""' required>
                  <option value="" disabled selected>Year</option>""")
      for num_years in range(year-10,year-101,-1):
         print("""<option value='""",num_years,"""'>""",num_years,"""</option>""")
      print("""
               </select>
            </div>
          </td>""")
      if(int(adl)>adlts_ and int(child)==0):
         print("""
          <tr><td style="position:absolute;color:white;height:0px;width:80%;margin: auto;left:0px;right:0px;background-color:grey;opacity:.3">'</td></tr>""")
      if(int(child)>0):
         print("""<tr><td style="position:absolute;color:white;height:0px;width:80%;margin: auto;left:0px;right:0px;background-color:grey;opacity:.3">'</td></tr>""")
      print("""
        </tr>
      </table>""")

   for child_ in range(1,int(child)+1):
      print("""
      
      
      <table style="width:100%;">
        <tr>
          <td>
            <H3 style="margin-bottom:0px;margin-left:50px;font-size:17px;">Child """,child_ ,"""</H2>
          </td>
        </tr>
        <tr>
          <td style="width:20%;">
            <H3 style="margin-top:10px;margin-left:80px;font-size:14px;">Name: </H3>
          </td>
          <td><input name='name2""",child_,"""' id='name2""",child_,"""' onchange="nameinarr2(""",child_,""");" class="name" type="text"  placeholder= "by ID"  required/></td>
        </tr>
        <tr>
          <td style="width:20%;">
            <H3 style="margin-top:10px;margin-left:80px;font-size:14px;">Surname: </H3>
          </td>
          <td><input name='surname2""",child_,"""' id='surname2""",child_,"""' onchange="nameinarr2(""",child_,""");" class="name" type="text" placeholder= "by ID"  required/></td>
        </tr>
        <tr>
          <td style="width:20%;">
            <H3 style="margin-top:10px;margin-left:80px;font-size:14px;">Gender: </H3>
          </td>
          <td style="width:50%;">
            <div style="float: left; width: 80px;" class="styled-select">
               <select id="gender" required>
                  <option value="" disabled selected>Select</option>
                  <option>Male</option>
                  <option>Female</option>
               </select>
            </div>
          </td>
          <td></td>
        </tr>
        <tr>
          <td style="width:20%;border:">
            <H3 style="margin-top:10px;margin-left:80px;font-size:14px;">Date of birth: </H3>
          </td>
          <td style="width:20%;">
            <div  style="float: left; width: 66px;" class="styled-select">
               <select name='day""",child_,"""' required>
                  <option value="" disabled selected>Day</option>""")
      for num_days in range(1,32):
         print("""<option value='""",num_days,"""'>""",num_days,"""</option>""")
      print("""
               </select>
            </div>
            <div  style="float: left; width: 66px;" class="styled-select">
               <select name='month""",child_,"""' onchange="callchild('err""",child_,"""','day""",child_,"""','month""",child_,"""','year""",child_,"""','errcheck""",child_,"""')" required>
                  <option value="" disabled selected>Month</option>
                     <option value="1">Jan</option> 
                     <option value="2">Feb</option> 
                     <option value="3">Mar</option> 
                     <option value="4">Apr</option> 
                     <option value="5">May</option> 
                     <option value="6">Jun</option> 
                     <option value="7">Jul</option> 
                     <option value="8">Aug</option> 
                     <option value="9">Sep</option> 
                     <option value="10">Oct</option> 
                     <option value="11">Nov</option> 
                     <option value="12">Dec</option> 
               </select>
            </div>
            <div  style="float: left; width: 66px;" class="styled-select">
                <select name='year""",child_,"""' onchange="callchild('err""",child_,"""','day""",child_,"""','month""",child_,"""','year""",child_,"""','errcheck""",child_,"""')" required>
                  <option value="" disabled selected>Year</option>""")
      for num_years in range(year,year-11,-1):
         print("""<option value='""",num_years,"""'>""",num_years,"""</option>""")
      print("""
               </select>
            </div>
          </td>
          <tr><td></td><td><input id='errcheck""",child_,"""' name='errcheck""",child_,"""' value=' ' style="position:absolute;margin-left:-45px;z-index:-900;opacity:0;" required/></td></tr>
          <tr><td></td><td name='err""",child_,"""' style="color:red;font-size:14px;padding-left:10px;"></td></tr>""")
      if(int(child)>child_):
         print("""
          <tr><td style="position:absolute;color:white;height:0px;width:80%;margin: auto;left:0px;right:0px;background-color:grey;opacity:.3">'</td></tr>""")
      print("""
        </tr>
      </table>""")      

   print("""

     

			  <div id="empty-div">""</div>
      
     <input class="get_var_invisible" name="days_dif1" id="days_dif1" value='""",days_dif1,"""'/>""")
   if radio != " 1 ":
      print("""<input class="get_var_invisible" name="days_dif2" id="days_dif2" value='""",days_dif2,"""'/>
               <input class="get_var_invisible" name="coll2" id="coll2" value='""",coll2,"""'/>
               <input class="get_var_invisible" name="end_date" id="end_date" value='""",end_date,"""'/>
               <input class="get_var_invisible" name="fare2" id="fare2" value='""",fare2,"""'/>
               <input class="get_var_invisible" name="dest2" id="dest2" value='""",dest2,"""'/>""")
   print("""
     <input class="get_var_invisible" name="coll1" id="coll1" value='""",coll1,"""'/>
     <input class="get_var_invisible" name="array1" id="array1" value=''/>
     <input class="get_var_invisible" name="array2" id="array2" value=''/>
     <input class="get_var_invisible" name="names" id="names" value=''/>
     <input class="get_var_invisible" name="surnames" id="surnames" value=''/>
     <input class="get_var_invisible" name="radio" value='""",radio,"""'/>
     <input class="get_var_invisible" name="adl" value='""",adl,"""'/>
     <input class="get_var_invisible" name="start_dest" value='""",start_dest,"""'/>
     <input class="get_var_invisible" name="end_dest" value='""",end_dest,"""'/>
     <input class="get_var_invisible" name="dest1" id="dest1" value='""",dest1,"""'/>
     <input class="get_var_invisible" name="fare" id="fare" value='""",fare,"""'/>
     <input class="get_var_invisible" name="fare1" id="fare1" value='""",fare1,"""'/>
     <input class="get_var_invisible" name="start_date" id="start_date" value='""",start_date,"""'/>
      
      <button id="results-select-pos" class="button3">""")
   if(int(seats_num)==1):
      print("""Buy Ticket Now</button>""")
   else:
      print("""Buy Tickets Now</button>""")
   print("""
      <div id="empty-div" style="opacity:0">""</div>
      
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
   </html>""")
conn.close()