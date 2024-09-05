import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email Configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "your_email@gmail.com"
receiver_email = "recipient_email@example.com"
password = "your_password"

# SMTP_SERVER=mail.belto.site
# SMTP_PORT=465
# SMTP_USER=outreach@belto.site
# SMTP_PASSWORD=pbJ01I$71TnR

# Create the Email Object
message = MIMEMultipart("alternative")
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "HTML Email with Arguments"

# HTML Content with Placeholders for Input Arguments
html_content = """
<html>
  <body>
    <h1>Welcome, {name}!</h1>
    <p>This is a test email sent from Python.</p>
    <p>Here is a special offer just for you: <b>{offer}</b></p>
    <p>Visit our website at: <a href="{website_url}">{website_name}</a></p>
  </body>
</html>
"""

# Input Arguments for the HTML Template
name = "John Doe"
offer = "50% off on your next purchase!"
website_url = "https://www.example.com"
website_name = "Our Website"

# Replace Placeholders with Actual Values
html_body = html_content.format(name=name, offer=offer, website_url=website_url, website_name=website_name)

# Attach the HTML body to the email
message.attach(MIMEText(html_body, "html"))

# Send the Email
try:
    # Connect to the Gmail SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Start the encryption process

    # Login to the email account
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())

    print("HTML email sent successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the connection
    server.quit()

