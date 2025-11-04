import smtplib
from email.mime.text import MIMEText
def sendMail(recipient, subj, bodyHtml):
    sender_email = "is21d005@mandakh.edu.mn"
    sender_password = "05060109"
    recipient_email = recipient
    subject = subj
    body = bodyHtml
    html_message = MIMEText(body, 'html')
    html_message['Subject'] = subject
    html_message['From'] = sender_email
    html_message['To'] = recipient_email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, html_message.as_string())
#sendMail