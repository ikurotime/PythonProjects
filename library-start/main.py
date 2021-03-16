from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []
length = 0
@app.route('/')
def home():
    return render_template('index.html',books= all_books, len_list=length)


@app.route("/add",methods = ['GET', 'POST'])
def add():
    return render_template('add.html')

@app.route("/add/success",methods = ['GET','POST'])
def add_book():
    global length
    name = request.form['name']
    author = request.form['author']
    rating = request.form['rating']
    all_books.append(
            {
                "title": name,
                "author": author,
                "rating": int(rating)
            }
    )
    length += 1
    return redirect(url_for('home'))
if __name__ == "__main__":
    app.run(debug=True)

