import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


smtp_port = 587
smtp_server = "smtp.gmail.com"

email_from = "issakzadedavid@gmail.com"
email_to = "david.issak-zade@mail.ru"


# Access the password EXTERNALLY
def GetPassword():
    with open("gmailapppass.txt", "r") as passwordFile:
        return passwordFile.read()


pswd = GetPassword()

subject = "Here is your book!"


def send_book(bookname, author, pages, genre):
    body = f"""
        You have searched for book: {bookname}
        Author: {author} 
        Genre: {genre}
        Length: {str(pages)}

"""

    # Make a MIME object to define paarats of the email
    msg = MIMEMultipart()
    msg["From"] = email_from
    msg["To"] = email_to
    msg["Subject"] = subject

    # Attach the body of the message
    msg.attach(MIMEText(body, 'plain'))

    filename = "Master-Your-Emotions.epub"
    attachment = open(filename, 'rb')

    # Encode the epub file as base 64
    book_package = MIMEBase('application', 'octet-stream')
    book_package.set_payload(attachment.read())
    encoders.encode_base64(book_package)
    book_package.add_header('Content-Disposition',
                            'attachment; filename= ' + filename)
    msg.attach(book_package)

    EmailTXT = msg.as_string()
    print(type(EmailTXT))
    print(EmailTXT)
    # Connect to the server
    print("Connecting to gmail server...")
    GmailServer = smtplib.SMTP(smtp_server, smtp_port)
    GmailServer.starttls()
    GmailServer.login(email_from, pswd)
    print("Succesfully connected to server!\n")

    print(f"Sending email to - {email_to}")
    GmailServer.sendmail(email_from, email_to, EmailTXT)
    print("mail sent succesfully")

    GmailServer.quit()


send_book("master your emotions", "david", 100, "self")
