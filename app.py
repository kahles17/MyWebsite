from flask import Flask,request
from flask_cors import CORS, cross_origin
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
def send_email(imagefile):
    msg = EmailMessage()
    msg['subject']='Reporting'
    msg['From']='simon@ayhamcloud.de'
    msg['To']='simon.roehrl01@gmail.com'
    msg.set_content('Bild befindet sich im Anhang')
    imagefile.save("image.png")
    files = ['image.png']

    for file in files:
        with open(file,'rb') as f:
            file_data = f.read()
            file_name = f.name
            print("file received")
    msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)
    print("added attachment")
    with smtplib.SMTP_SSL('mail.ayhamcloud.de',465) as smtp:
        print("connection to smtp")
        smtp.login("simon@ayhamcloud.de","Simon$$")
        print("logged into gmail")
        smtp.send_message(msg)
        print("sent message")

@app.route('/', methods=['POST'])
@cross_origin()
def form():
    imagefile = request.files['imagefile']
    send_email(imagefile)
    return request.form

if __name__ == "__main__":
    app.run(debug=True)
