from email.mime import multipart
from flask import Flask,request
from flask_cors import CORS, cross_origin
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
sender_email = "webdesign.gessulat@gmail.com"
password = "nekqlfohadsebjqn"
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
def send_email(imagefile,html,email):
    message = MIMEMultipart("alternative")
    message['Subject']='Reporting'
    message['From']='webdesign.gessulat@gmail.com'
    message['To']=email
    html = MIMEText(html, "html")
    message.attach(html)
    imagefile.save("image.png")


        with open("image.png",'rb') as f:
        file_data = f.read()
        file_name = f.name
        print("file received")
        image = MIMEImage(file_data,name=file_name)
        message.attach(image)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, email, message.as_string()
            )

@app.route('/', methods=['POST'])
@cross_origin()
def form():
    imagefile = request.files['imagefile']
    html = request.form['html']
    email = request.form['email']
    send_email(imagefile,html,email)
    return request.form

if __name__ == "__main__":
    app.run()
