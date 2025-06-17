# Day 32: Email SMPT and Date Time module 

# Simple Mail Transfer Protocol smtplib 

# Sender → Sender’s Mail Server → Recipient’s Mail Server → Recipient’s Inbox

# This transfer is governed by SMTP (Simple Mail Transfer Protocol).

# smtplib – Sending Emails via SMTP




import datetime
today = datetime.datetime.now()

print(today)
# DateTime


# Module	    Purpose	                    Key Methods	                                        Used For
# smtplib	    Send emails using           SMTP	SMTP(), starttls(), login(), sendmail()	    Automating email sending
# datetime	    Work with date and time	    now(), today, .month, .day	                        Check if today matches a birthday