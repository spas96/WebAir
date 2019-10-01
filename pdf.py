#! /Python34/python

print("Content-type: text/html \n")

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
from reportlab.lib.colors import HexColor

def generate_tickets(first_name,last_name,pdf_file_name,seat_id,dest,dateoft):
   c = canvas.Canvas(pdf_file_name, pagesize=landscape(letter))
   pic = 'logo.png'
   c.drawImage(pic,320,500,width=150, height=90)
   c.setFont('Helvetica', 46, leading=None)
   c.drawCentredString(396,430,"Your ticket")
   c.drawCentredString(396,380,"12345")
   c.setFont('Helvetica', 30, leading=None)
   c.drawCentredString(396,300,dest)
   c.drawCentredString(396,260,dateoft)
   c.drawCentredString(396,220,first_name+" "+last_name)
   c.drawCentredString(396,180,"Seat: "+seat_id)
   print("2")
   c.showPage()
   print("writing")
   c.save()
   
generate_tickets("Spas","Spasov","tickets/1.pdf","3","Manchester - Bristol - 12:20:00","03/15/2016")