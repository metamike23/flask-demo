import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set up the email sender, receiver, and server
smtp_server = "smtp.gmail.com"
smtp_port = 587  # Gmail SMTP port
sender_email = "your_email@gmail.com"
receiver_email = "recipient_email@example.com"
password = "your_password"  # If using 2-factor authentication, use an App Password here

# Create the message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test Email"

# Add the body of the email
body = "This is a test email sent from Python!"
message.attach(MIMEText(body, "plain"))

try:
    # Connect to the Gmail SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection

    # Log in to the email account
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email sent successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the connection
    server.quit()
