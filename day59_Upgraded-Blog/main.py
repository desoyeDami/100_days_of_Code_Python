from flask import Flask, render_template, request
import requests
import smtplib

MY_EMAIL = "desoyee@gmail.com"
PASSWORD = "wtvyqllmhffvuggh"
RECIPIENT_MAIL = "desoyedami@gmail.com"

blog_url = "https://api.npoint.io/a49109ad9e74ae4d57f0"
response = requests.get(blog_url)
blog_data = response.json()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", blogs=blog_data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    success_msg = True
    if request.method == 'POST':
        new_connection = request.form
        name = new_connection["name"]
        mail = new_connection["mail"]
        phone_number = new_connection["tel"]
        message = new_connection["msg"]
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=RECIPIENT_MAIL,
                                msg=f"Subject: New Blog Connection\n\nName: {name}\n"
                                    f"Mail: {mail}\n"
                                    f"Phone Number: {phone_number}\n"
                                    f"Message: {message}")
        return render_template("contact.html", msg=success_msg)
    return render_template("contact.html")


@app.route("/post/<int:id>")
def post(id):
    post_requested = None
    for blog_post in blog_data:
        if blog_post["id"] == id:
            post_requested = blog_post
    return render_template("post.html", blog=post_requested)


if __name__ == "__main__":
    app.run(debug=True)
