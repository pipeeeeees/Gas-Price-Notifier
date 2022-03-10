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
import credentials


def sendEmail(recipient, subject, message):
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(str(os.environ.get('GMAIL_USER')), str(os.environ.get('GMAIL_PASS')))
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = "pipeeeeees@gmail.com"
    msg['To'] = recipient
    s.send_message(msg)
    s.quit()