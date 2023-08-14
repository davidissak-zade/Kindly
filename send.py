import smtplib
import ssl
from email.message import EmailMessage

smtp_port = 587
smtp_server = "smtp.gmail.com"

email_from = "issakzadedavid@gmail.com"
email_to = "issakzadedavid@gmail.com"


# Access the password EXTERNALLY
def GetPassword():
    with open("gmailapppass.txt", "r") as passwordFile:
        return passwordFile.read()


pswd = GetPassword()

message = "The book you were searching for is attached in epub format."

newMessage = EmailMessage()
newMessage["Subject"] = "Here is your book!"
newMessage.set_content(message)


simple_email_context = ssl.create_default_context()

try:
    print("Connecting to gmail server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_from, pswd)
    print("connected to server \n")

    print(f"Sending emails from  - {email_from}")
    print(f"Sending email to - {email_to}")
    TIE_server.sendmail(email_from, email_to, newMessage.as_string())
    print("mail sent succesfully")
except Exception as e:
    print(e)

finally:
    TIE_server.quit()
