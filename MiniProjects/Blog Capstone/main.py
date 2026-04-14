from flask import Flask, render_template, request
from post import Post
from datetime import datetime
import requests
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__, static_folder='static')

posts_url = "https://api.npoint.io/c790b4d5cab58020d391"
all_posts = requests.get(posts_url).json()
post_objects = []
for post in all_posts:
    post_objects.append(Post(id=post['id'], body=post['body'], title=post['title'], subtitle=post['subtitle']))

@app.route('/')
def home():
    current_date = datetime.now().strftime('%Y-%m-%d')
    return render_template("index.html", posts = all_posts, date = current_date)

@app.route('/post/<int:id>')
def get_post(id):
    for post in post_objects:
        if post.id == id:
            return render_template("blog-details.html", post = post)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        form_dict = {
            "name" : request.form["name"],
            "email" : request.form["email"],
            "subject" : request.form["subject"],
            "message" : request.form["message"],
        }

        msg=MIMEText(form_dict["message"])
        msg["Subject"] = form_dict["subject"]
        msg["From"] = os.environ["GMAIL_EMAIL"]
        msg["To"] = form_dict["email"]
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(os.environ["GMAIL_EMAIL"], os.environ["GMAIL_PASS"])
            smtp_server.sendmail(os.environ["GMAIL_EMAIL"], form_dict["email"], msg.as_string())
            print("Message sent!")

        return render_template("contact.html", details=form_dict)

    elif request.method == "GET":
        return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
