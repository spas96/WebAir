#! /Python34/python

import os
import smtplib
import string
import sys
print("Content-type: text/html \n")
 
 
from configobj import ConfigObj
from email import Encoders
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.Utils import formatdate
 
#----------------------------------------------------------------------
def send_email_with_attachment(subject, body_text, to_emails,
                               cc_emails, bcc_emails, file_to_attach):
    """
    Send an email with an attachment
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "config.ini")
    header = 'Content-Disposition', 'attachment; filename="%s"' % file_to_attach
 
    # get the config
    if os.path.exists(config_path):
        cfg = ConfigObj(config_path)
        cfg_dict = cfg.dict()
    else:
        print "Config not found! Exiting!"
        sys.exit(1)
 
    # extract server and from_addr from config
    host = cfg_dict["smtp"]["server"]
    from_addr = cfg_dict["smtp"]["from_addr"]
 
    # create the message
    msg = MIMEMultipart()
    msg["From"] = from_addr
    msg["Subject"] = subject
    msg["Date"] = formatdate(localtime=True)
    if body_text:
        msg.attach( MIMEText(body_text) )
 
    msg["To"] = ', '.join(to_emails)
    msg["cc"] = ', '.join(cc_emails)
 
    attachment = MIMEBase('application', "octet-stream")
    try:
        with open(file_to_attach, "rb") as fh:
            data = fh.read()
        attachment.set_payload( data )
        Encoders.encode_base64(attachment)
        attachment.add_header(*header)
        msg.attach(attachment)
    except IOError:
        msg = "Error opening attachment file %s" % file_to_attach
        print msg
        sys.exit(1)
 
    emails = to_emails + cc_emails
 
    server = smtplib.SMTP(host)
    server.sendmail(from_addr, emails, msg.as_string())
    server.quit()
 
if __name__ == "__main__":
    emails = ["mike@somewhere.org", "nedry@jp.net"]
    cc_emails = ["someone@gmail.com"]
    bcc_emails = ["anonymous@circe.org"]
 
    subject = "Test email with attachment from Python"
    body_text = "This email contains an attachment!"
    path = "/path/to/some/file"
    send_email_with_attachment(subject, body_text, emails, 
                               cc_emails, bcc_emails, path)