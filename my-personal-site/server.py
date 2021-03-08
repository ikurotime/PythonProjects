from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route("/login",methods=["POST"])
def receive_data():
    name = request.form["name"]
    mail = request.form["email"]
    message = request.form["message"]
    return f"<h1>Name: {name}, mail: {mail},message:{message}</h1>"
if __name__ == "__main__":
    app.run(debug=True)