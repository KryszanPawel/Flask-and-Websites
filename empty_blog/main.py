from flask import Flask, render_template, request
import requests
from datetime import datetime
import smtplib

USER = ""         #Input dummy email to send contact form from
PASSWORD = ""              #Password to log in  to dummy email
YOUR_EMAIL = ""   #Email you want to send notification to.

app = Flask(__name__)

response = requests.get("https://api.npoint.io/7ab7877c456d92deb6d2").json()    # my dummy endpoint with posts
date = datetime.today().strftime("%Y-%m-%d")

def send_email(name,email,phone, message):
    with smtplib.SMTP("smtp.office365.com", port=587) as connection:    # details for hotmail.com
        connection.starttls()
        connection.login(user=USER, password=PASSWORD)
        connection.sendmail(from_addr=USER,
                            to_addrs=YOUR_EMAIL,
                            msg=f"Subject:New Message\n\nName: {name}\nE-mail: {email}\nPhone: {phone}\nMessage: {message}")

@app.route("/")
def main():
    # requests for data

    return render_template("index.html", response=response, date=date)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "GET":
        title = 0
        return render_template("contact.html", title= title)
    elif request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        if name and email and phone and message:
            title = "Successfully sent your message"
            send_email(name, email, phone, message)
        else:
            title = "Something went wrong, please fill the form once again"
        return render_template("contact.html", title=title)


@app.route("/post/id/<id>")
def post(id):
    id = int(id)
    return render_template("post.html", posts=response, id=id, date=date)



if __name__=="__main__":

    app.run(debug=True)