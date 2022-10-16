from email.message import EmailMessage
import smtplib
import ssl
import Constants as keys

def sendemail(destEmail, userSubject, userContent):
    """ This function sends an email to one or multiple user emails """
    # Create the mail object
    em = EmailMessage()
    em['From'] = keys.EMAIL_SENDER
    em['To'] = destEmail
    em['Subject'] = userSubject
    em.set_content(userContent)

    # Send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        # Login to send email
        smtp.login(keys.EMAIL_SENDER, keys.EMAIL_SENDER_PASSWORD)
        # Send email
        smtp.sendmail(keys.EMAIL_SENDER, destEmail, em.as_string())
