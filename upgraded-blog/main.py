from flask import Flask,render_template
import requests

post = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

print(post[0]['title'])
app = Flask(__name__)

@app.route("/")
def get_all_posts():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:num>")
def post(num):
    post_title = post[num]['title']
    post_subtitle = post[num]['subtitle']
    post_author = post[num]['author']
    post_date = post[num]['date']
    return render_template("post.html",title= post_title, subtitle=post_subtitle, author=post_author,date=post_date)


if __name__ == "__main__":
    app.run(debug = True)