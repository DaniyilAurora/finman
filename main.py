from flask import Flask, render_template
from database import Database

database = Database()

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html", name="test")

if __name__ == "__main__":
    app.run(debug=True)