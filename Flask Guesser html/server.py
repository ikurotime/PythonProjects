from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route("/guess/<name>")
def guess(name):
    def guess_gender():
        response = requests.get(f"https://api.genderize.io?name={name}")
        data = response.json()
        gender = data['gender']
        return gender
    def guess_age():
        response = requests.get(f"https://api.agify.io?name={name}")
        data = response.json()
        age = data['age']
        return age
    return render_template("index.html", name= name, age = guess_age(), gender = guess_gender())

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(blog_url)
    all_post = response.json()
    return render_template("blog.html", posts= all_post)
if __name__ == "__main__":
    app.run(debug = True)