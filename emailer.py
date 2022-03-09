# -*- coding: utf-8 -*-
"""
Title:      emailer.py
Purpose:    this .py file handles the emailing service, namely Gmail, to send
            an email from my email address, pipeeeeees@gmail.com, to a 
            recipient address. Gmail app password stored in env.
    
Author:     D. Pipes
IDE:        Spyder 5
Created:    3/8/2022
"""

from email.message import EmailMessage
import smtplib
import os

gmail_user = os.environ.get('GMAIL_USER')
gmail_pass = os.environ.get('GMAIL_PASS')

def sendEmail(recipient, subject, message):
    global gmail_user
    global gmail_pass
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(gmail_user, gmail_pass)
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = "pipeeeeees@gmail.com"
    msg['To'] = recipient
    s.send_message(msg)
    s.quit()