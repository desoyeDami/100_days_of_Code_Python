from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
blog_response = requests.get(blog_url)
blog_data = blog_response.json()


@app.route('/')
def home():
    return render_template("index.html", blog_posts=blog_data)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in blog_data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
