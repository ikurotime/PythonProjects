from flask import Flask,render_template,request
from smtplib import SMTP
import os

app = Flask(__name__)
MAIL = os.environ.get('BOT_MAIL')
PSWD = os.environ.get('MY_PSWD')
TO_MAIL = os.environ.get('MY_MAIL')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/success",methods=["POST"])
def receive_data():

    name = request.form["username"]
    mail = request.form["email"]
    message = request.form["message"]
    send_data(s_mail = mail,s_name = name,s_msg = message)
    return render_template('success.html')

def send_data(s_mail,s_name,s_msg):
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = MAIL,password = PSWD)
        connection.sendmail(from_addr = MAIL,
                            to_addrs = TO_MAIL,
                            msg = ("Subject:Mail from web\n\n"
                                  f"From: {s_mail}\n"
                                  f"Name: {s_name}\n"
                                  f"Msg: {s_msg}").encode('utf-8'))
if __name__ == "__main__":
    app.run(debug=True)