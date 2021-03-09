from flask import Flask,render_template
from datetime import *

app = Flask(__name__)
year= datetime.now().year
print(year)
@app.route("/")
def home():
    return render_template('index.html', year= year)


if __name__ == "__main__":
    app.run(debug = True)