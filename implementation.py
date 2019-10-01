#! /Python34/python

import cgi, cgitb, sys, mysql.connector, datetime, smtplib, math
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from datetime import date
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
print("Content-type: text/html \n")

def generate_tickets(pdf_file_name,first_name,last_name,seat_id,dest,dateoft,ticket_num):
   c = canvas.Canvas(pdf_file_name, pagesize=landscape(letter))
   pic = 'logo.png'
   c.drawImage(pic,320,500,width=150, height=90)
   c.setFont('Helvetica', 46, leading=None)
   c.drawCentredString(396,430,"Your ticket")
   c.drawCentredString(396,380,ticket_num)
   c.setFont('Helvetica', 30, leading=None)
   c.drawCentredString(396,300,dest)
   c.drawCentredString(396,260,dateoft)
   c.drawCentredString(396,220,first_name+" "+last_name)
   c.drawCentredString(396,180,"Seat: "+seat_id)
   c.showPage()
   c.save()
   
def send_email(file_name,email_to_send):
   emailfrom = "uwewebair@gmail.com"
   emailto = email_to_send
   fileToSend = file_name
   username = "uwewebair"
   password = "uwewebair1"

   msg = MIMEMultipart()
   msg["From"] = emailfrom
   msg["To"] = emailto
   msg["Subject"] = "WebAir-Ticket"


   ctype = "application/octet-stream"
   maintype, subtype = ctype.split("/", 1)

   fp = open(fileToSend, "rb")
   attachment = MIMEBase(maintype, subtype)
   attachment.set_payload(fp.read())
   fp.close()
   encoders.encode_base64(attachment)
   attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
   msg.attach(attachment)

   server = smtplib.SMTP("smtp.gmail.com:587")
   server.starttls()
   server.login(username,password)
   server.sendmail(emailfrom, emailto, msg.as_string())
   server.quit()

cgitb.enable()

form = cgi.FieldStorage()

now = datetime.datetime.now()
y = now.year
mon = now.month
d = now.day
h = now.hour
min = now.minute
s = now.second

radio = form.getvalue('radio').strip() #if none -> invalid sesion search again
email = form.getvalue('email').strip()
names = form.getvalue('names')
names = names.split(',')
surnames = form.getvalue('surnames')
surnames = surnames.split(',')
adl = form.getvalue('adl')
adl = int(adl)
dest1 = form.getvalue('dest1')
start_dest = form.getvalue('start_dest').strip()
end_dest = form.getvalue('end_dest').strip()
fare = form.getvalue('fare')
fare1 = form.getvalue('fare1')
coll1 = form.getvalue('coll1').strip()
days_dif1 = form.getvalue('days_dif1')
start_date = form.getvalue('start_date')
array1 = form.getvalue('array1')
array1 = array1.split(',')
array1 = [int(i) for i in array1]
if radio != "1":
   dest2 = form.getvalue('dest2')
   fare2 = form.getvalue('fare2')
   end_date = form.getvalue('end_date')
   array2 = form.getvalue('array2')
   array2 = array2.split(',')
   array2 = [int(i) for i in array2]
   days_dif2 = form.getvalue('days_dif2')
   coll2 = form.getvalue('coll2').strip()


conn = mysql.connector.connect(host='localhost',
                              database='webair',
                              user='root',
                              password='')


if conn.is_connected():
   cursor1 = conn.cursor(buffered=True)
   query1 = """SELECT jt_seats_available FROM `journey_times` 
              WHERE jt_leave_destination = %s AND jt_arrive_destination = %s AND jt_leave_time = %s"""
   args1 = (start_dest,end_dest,coll1[-8:])
   cursor1.execute(query1,args1)
   row1 = cursor1.fetchone()
   row1 = str(row1)
   row1 = row1.replace("(", "")
   row1 = row1.replace(")", "")
   row1 = row1.replace(",", "")
   cursor = conn.cursor()
   query = """ UPDATE `journey_times`
               SET jt_seats_available = %s
               WHERE jt_leave_destination = %s AND jt_arrive_destination = %s AND jt_leave_time = %s"""
   args = (int(row1)-(len(array1)),start_dest,end_dest,coll1[-8:])
   cursor.execute(query,args)
   conn.commit()    
   cursor.close()
   cursor1.close()
   for i in range(0,len(array1)):
      cursor = conn.cursor()
      query = """ UPDATE `"""+coll1+"""`
                SET d"""+str(days_dif1).strip()+""" = %s
                WHERE seat_id = %s """
      (taken, seatid) = (0, array1[i])
      args = (taken, seatid)
      cursor.execute(query,args)  
      conn.commit()    
      cursor.close()
      cursor = conn.cursor()
      query = """ INSERT INTO `tickets` (`email`, `first_name`, `second_name`, `seat_id`, `dest`, `price`, `byear`, `bmonth`, `bday`, `bhour`, `bmin`, `bsec`, `depart`, `return_`, `days_dif`) VALUES
                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
      if i >= adl and adl > 0:
         args = (email, names[i].strip(), surnames[i].strip(), array1[i], coll1, int(float(fare1)-float(fare1)*0.2), y, mon, d, h, min, s,start_dest,end_dest,days_dif1)
      else:
         args = (email, names[i].strip(), surnames[i].strip(), array1[i], coll1, int(float(fare1)), y, mon, d, h, min, s,start_dest,end_dest,days_dif1)
      cursor.execute(query,args)
      conn.commit()    
      cursor.close()
      cursor = conn.cursor()
      query = """SELECT id FROM `tickets` WHERE seat_id = %s AND dest = %s AND byear = %s AND bmonth = %s AND bday = %s AND bhour = %s AND bmin = %s AND bsec = %s"""
      args = (array1[i], coll1, y, mon, d, h, min, s)
      cursor.execute(query,args)
      row = cursor.fetchone()
      row = str(row)
      row = row.replace("(", "")
      row = row.replace(")", "")
      row = row.replace(",", "")
      row = int(row)
      row = "{0:0=5d}".format(row)
      generate_tickets("tickets/"+names[i].strip()+"_"+surnames[i].strip()+"_1.pdf",names[i].strip(),surnames[i].strip(),str(array1[i]),coll1,start_date,row)
      send_email("tickets/"+names[i].strip()+"_"+surnames[i].strip()+"_1.pdf",email)
      conn.commit()    
      cursor.close()
   if radio != "1":
      cursor1 = conn.cursor(buffered=True)
      query1 = """SELECT jt_seats_available FROM `journey_times` 
                 WHERE jt_leave_destination = %s AND jt_arrive_destination = %s AND jt_leave_time = %s"""
      args1 = (end_dest,start_dest,coll2[-8:])
      cursor1.execute(query1,args1)
      row1 = cursor1.fetchone()
      row1 = str(row1)
      row1 = row1.replace("(", "")
      row1 = row1.replace(")", "")
      row1 = row1.replace(",", "")
      cursor = conn.cursor()
      query = """ UPDATE `journey_times`
                  SET jt_seats_available = %s
                  WHERE jt_leave_destination = %s AND jt_arrive_destination = %s AND jt_leave_time = %s"""
      args = (int(row1)-(len(array2)),end_dest,start_dest,coll2[-8:])
      cursor.execute(query,args)
      conn.commit()    
      cursor.close()
      cursor1.close()
      for i in range(0,len(array2)):
         cursor = conn.cursor()
         query = """ UPDATE `"""+coll2+"""`
                   SET d"""+str(days_dif2).strip()+""" = %s
                   WHERE seat_id = %s """
         (taken, seatid) = (0, array2[i])
         args = (taken, seatid)

         cursor.execute(query,args)  
         conn.commit()    
         cursor.close()
         cursor = conn.cursor()
         query = """ INSERT INTO `tickets` (`email`, `first_name`, `second_name`, `seat_id`, `dest`, `price`, `byear`, `bmonth`, `bday`, `bhour`, `bmin`, `bsec`, `depart`, `return_`, `days_dif`) VALUES
                   (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
         if i >= adl and adl > 0:
            args = (email, names[i].strip(), surnames[i].strip(), array2[i], coll2, int(float(fare2)-float(fare1)*0.2), y, mon, d, h, min, s,start_dest,end_dest,days_dif2)
         else:
            args = (email, names[i].strip(), surnames[i].strip(), array2[i], coll2, int(float(fare2)), y, mon, d, h, min, s,start_dest,end_dest,days_dif2)
         cursor.execute(query,args)
         conn.commit()    
         cursor.close()
         cursor = conn.cursor()
         query = """SELECT id FROM `tickets` WHERE seat_id = %s AND dest = %s AND byear = %s AND bmonth = %s AND bday = %s AND bhour = %s AND bmin = %s AND bsec = %s"""
         args = (array2[i], coll2, y, mon, d, h, min, s)
         cursor.execute(query,args)
         row = cursor.fetchone()
         row = str(row)
         row = row.replace("(", "")
         row = row.replace(")", "")
         row = row.replace(",", "")
         row = int(row)
         row = "{0:0=5d}".format(row)
         generate_tickets("tickets/"+names[i].strip()+"_"+surnames[i].strip()+"_2.pdf",names[i].strip(),surnames[i].strip(),str(array2[i]),coll2,start_date,row)
         send_email("tickets/"+names[i].strip()+"_"+surnames[i].strip()+"_2.pdf",email)
         conn.commit()    
         cursor.close()


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
						<a href="#/webprog/WebAir/manage_ticket.py" id="manage" class="button-top">Manage Ticket</a>
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

  """,radio+coll1+"""d"""+str(days_dif1).strip(),array1,len(array1),email," ",names," ",surnames," ",dest1," ",fare," ",y," ","{0:0=2d}".format(mon)," ","{0:0=2d}".format(d)," ","{0:0=2d}".format(h)," ","{0:0=2d}".format(min)," ","{0:0=2d}".format(s),start_date)
if radio != "1":
   print(dest2,end_date)
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