from flask import Flask, render_template
import requests


app = Flask(__name__)


blog_url = "https://api.npoint.io/ed99320662742443cc5b"
all_posts = requests.get(blog_url).json()

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:id>')
def post(id):
    post = all_posts[id-1]
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
