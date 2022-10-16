from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

response = requests.get("https://api.npoint.io/7ab7877c456d92deb6d2").json()
date = datetime.today().strftime("%Y-%m-%d")



@app.route("/")
def main():
    # requests for data

    return render_template("index.html", response=response, date=date)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/id/<id>")
def post(id):
    id = int(id)
    return render_template("post.html", posts=response, id=id, date=date)


if __name__=="__main__":

    app.run(debug=True)