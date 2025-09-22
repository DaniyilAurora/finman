from flask import Flask, render_template
from database import Database
from datetime import datetime

database = Database()

app = Flask(__name__)

@app.route("/")
def hello():
    records = database.get_records()
    return render_template("index.html", rows=records)

if __name__ == "__main__":
    app.run(debug=True)