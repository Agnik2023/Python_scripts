import csv
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
from email_validator import validate_email, EmailNotValidError
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import os  # For file path handling

# SMTP server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'agnik252004@gmail.com'
smtp_password = 'rrqa hcdy cnfz cncf'  

# Sender and subject configuration
sender = 'agnik252004@gmail.com'
subject = "A Fool's Greetings and Attachments!"

try:
    with open('test.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            email = row[0]
            name = row[1]
            try:
                validate_email(email)
            except EmailNotValidError:
                print(f"Invalid email: {email}")
                continue

            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = email
            msg['Subject'] = subject

            body = f'''
<html>
<head>
    <title>A Fool's Attachments</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 20px;
        }}
        .container {{
            background-color: #ffffff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            margin: 0 auto;
        }}
        p {{
            line-height: 1.6;
        }}
    </style>
</head>
<body>
    <div class="container">
        <p>Hark, good morning!</p>
        <p>A greeting most grand for {name}, from this humble fool's hand! May your day be as bright as a jester's bells, and as filled with joy as a pie-throwing revels! </p>
        <p>Have a splendid day, and may your troubles be as fleeting as a courtier's wig in a strong breeze!</p>
        <p>With a flourish and a wink, and some attachments!</p>
        <p>Agnik Das, Your Humble Fool</p>
    </div>
</body>
</html>
'''

            msg_text = MIMEText(body, 'html')
            msg.attach(msg_text)

            # Attach PDF
            # pdf_filename = "example.pdf"  # Replace with your PDF filename
            # pdf_path = os.path.join(os.getcwd(), pdf_filename) #Gets current working directory.
            # try:
            #     with open(pdf_path, "rb") as pdf_file:
            #         pdf_attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
            #         pdf_attachment.add_header("Content-Disposition", f"attachment; filename={pdf_filename}")
            #         msg.attach(pdf_attachment)
            # except FileNotFoundError:
            #     print(f"Warning: PDF file '{pdf_filename}' not found. Email will be sent without PDF.")

            # # Attach Image
            # image_filename = "example.jpg"  # Replace with your image filename
            # image_path = os.path.join(os.getcwd(), image_filename) #Gets current working directory.
            # try:
            #     with open(image_path, "rb") as image_file:
            #         image_attachment = MIMEImage(image_file.read())
            #         image_attachment.add_header("Content-Disposition", f"attachment; filename={image_filename}")
            #         msg.attach(image_attachment)
            # except FileNotFoundError:
            #     print(f"Warning: Image file '{image_filename}' not found. Email will be sent without image.")

            # # Attach Text File
            # text_filename = "example.txt"  # Replace with your text filename
            # text_path = os.path.join(os.getcwd(), text_filename) #Gets current working directory.
            # try:
            #     with open(text_path, "r") as text_file:
            #         text_attachment = MIMEText(text_file.read(), 'plain')
            #         text_attachment.add_header("Content-Disposition", f"attachment; filename={text_filename}")
            #         msg.attach(text_attachment)
            # except FileNotFoundError:
            #     print(f"Warning: Text file '{text_filename}' not found. Email will be sent without text.")

            try:
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(smtp_username, smtp_password)
                    server.send_message(msg)
                print(f'Email sent successfully to {email}')
            except Exception as e:
                print(f'Failed to send email to {email}. Error: {e}') 

except FileNotFoundError:
    print("Error: CSV file 'test.csv' not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")