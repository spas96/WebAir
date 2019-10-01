#! /Python34/python

# 4658586875160017


import cgi, cgitb, sys, mysql.connector
print("Content-type: text/html \n")

cgitb.enable()

form = cgi.FieldStorage()

radio = form.getvalue('radio').strip() #if none -> invalid sesion search again
start_dest = form.getvalue('start_dest')
end_dest = form.getvalue('end_dest')
# start_date = form.getvalue('start_date')
# end_date = form.getvalue('end_date')
# adl = form.getvalue('adl')
# adl = int(adl)
# child = form.getvalue('child')
# child = int(child)
# num = 0
# args = (start_dest,end_dest,)
# args1 = (end_dest,start_dest,)
coll1 = form.getvalue('coll1')
days_dif1 = form.getvalue('days_dif1')
array1 = form.getvalue('array1')
names = form.getvalue('names')
surnames = form.getvalue('surnames')
dest1 = form.getvalue('dest1')
fare = form.getvalue('fare')
adl = form.getvalue('adl')
start_date = form.getvalue('start_date')
fare1 = form.getvalue('fare1')
if radio != "1":
   array2 = form.getvalue('array2')
   days_dif2 = form.getvalue('days_dif2')
   coll2 = form.getvalue('coll2')
   dest2 = form.getvalue('dest2')
   end_date = form.getvalue('end_date')
   fare2 = form.getvalue('fare2')
   
   
   
conn = mysql.connector.connect(host='localhost',
                              database='webair',
                              user='root',
                              password='')


print("""

<html>
<head>
  <meta charset="utf-8">

<link rel="StyleSheet" href="payment.css" type="text/css" media="screen">
<link rel="stylesheet" href="creditcard.css">
<link rel="stylesheet" href="try.css">
<script type="text/javascript" src="http://code.jquery.com/jquery-1.7.2.min.js"></script>

<script type="text/javascript" src="creditcard.js"></script>
<script type="text/javascript">
    $(function() {
		var grayThemeCreditcard = creditcard.initialize(
					'.creditcard-wrapper.gray-theme .expiration-month-and-year',
					'.creditcard-wrapper.gray-theme .credit-card-number',
					'.creditcard-wrapper.gray-theme .security-code',
					'.creditcard-wrapper.gray-theme .card-type');
					
		$(".creditcard-gray-theme-submit").click(function(e) {
			e.preventDefault();	
			var output = grayThemeCreditcard.validate();
			if (output) {
			// Your validated credit card output
			console.log(output);
        }
      });
});
</script>

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
		<section class="creditcard-wrapper gray-theme">
  <form action="implementation.py" method="POST">
			<h3>Credit Card Payment</h3>
			<i>
				<div class="card-type" style="text-align:right;margin-top:10px;margin-right:10px;min-height:20px;margin-bottom:-15px"></div>
			</i>
			<div class="credit-card-wrapper">
				<div class="first-row form-group">
				<div class="col-sm-8 controls">
					<label class="control-label">Card Number</label>
					<input id="nums" oninput="validateNum();" class="number credit-card-number form-control"
					type="text" name="number"
					pattern="\d*"
					inputmode="numeric" autocomplete="cc-number" autocompletetype="cc-number" x-autocompletetype="cc-number"
					placeholder="&#149;&#149;&#149;&#149; &#149;&#149;&#149;&#149; &#149;&#149;&#149;&#149; &#149;&#149;&#149;&#149;" required>
				</div>
				<div class="col-sm-4 controls">
					<label class="control-label">CVV</label>
					<input class="security-code form-control"·
					inputmode="numeric"
					pattern="\d*"
					type="text" name="security-code"
					placeholder="&#149;&#149;&#149;" required>
				</div>
				</div>
				<div class="second-row form-group">
				<div class="col-sm-8 controls">
					<label for="name" class="control-label">Name on Card</label>
					<input id="name" oninput="validateAlpha();" class="billing-address-name form-control"
					type="text" name="name" 
					placeholder="Kevin Jones" required>
				</div>
				<div class="col-sm-4 controls">
					<label class="control-label">Expiration</label>
					<input class="expiration-month-and-year form-control"
					type="text" name="expiration-month-and-year"
					placeholder="MM / YY" required>
				</div>
    <div class="col-sm-8 controls" style="top:20px;">
					<label for="email" class="control-label">Email to receive tickets</label>
					<input id="email" class="billing-address-name form-control"
					type="email" name="email" 
					placeholder="example@domain.host" required>
				</div>
				</div>
			</div>""")
print(names,"   ",surnames," ",dest1," ",fare)
if radio != "1":
   print(dest2)
print("""
   
     <input class="get_var_invisible" name="days_dif1" id="days_dif1" value='""",days_dif1,"""'/>
     <input class="get_var_invisible" name="coll1" id="coll1" value='""",coll1,"""'/>
     <input class="get_var_invisible" name="names" id="names" value='""",names,"""'/>
     <input class="get_var_invisible" name="surnames" id="surnames" value='""",surnames,"""'/>
     <input class="get_var_invisible" name="start_dest" id="start_dest" value='""",start_dest,"""'/>
     <input class="get_var_invisible" name="end_dest" id="end_dest" value='""",end_dest,"""'/>
     <input class="get_var_invisible" name="dest1" id="dest1" value='""",dest1,"""'/>
     <input class="get_var_invisible" name="fare" id="fare" value='""",fare,"""'/>
     <input class="get_var_invisible" name="start_date" id="start_date" value='""",start_date,"""'/>
     <input class="get_var_invisible" name="fare1" id="fare1" value='""",fare1,"""'/>
     <input class="get_var_invisible" name="adl" id="adl" value='""",adl,"""'/>
     <input class="get_var_invisible" name="array1" id="array1" value='""",array1,"""'/>""")
if radio != "1":
   print("""     
     <input class="get_var_invisible" name="array2" id="array2" value='""",array2,"""'/>
     <input class="get_var_invisible" name="days_dif2" id="days_dif2" value='""",days_dif2,"""'/>
     <input class="get_var_invisible" name="dest2" id="dest2" value='""",dest2,"""'/>
     <input class="get_var_invisible" name="end_date" id="end_date" value='""",end_date,"""'/>
     <input class="get_var_invisible" name="fare2" id="fare2" value='""",fare2,"""'/>
     <input class="get_var_invisible" name="coll2" id="coll2" value='""",coll2,"""'/>""")
print("""
     <input class="get_var_invisible" name="radio" value='""",radio,"""'/>

           <button id="results-select-pos" class="button2" style="top:20px;">Submit</button>
      
      </form>
		</section>
		

   
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
conn.commit()
conn.close()