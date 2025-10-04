from flask import Flask, request, render_template, redirect, url_for
from database import Database
from datetime import datetime

database = Database()

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    # If there is new request to add
    if request.method == 'POST':
        form_name = request.form.get("form_name")
        
        if form_name == "add":
            # Getting data from the post request
            amount = float(request.form['amount'])
            description = request.form['description']
            category = request.form['category']

            # Processing the data
            database.add_record(amount, description, category, datetime.now())
        elif form_name == "delete":
            # Getting data from the post request
            id = int(request.form['id'])

            # Processing the data
            database.delete_record(id)
        
        return redirect(url_for("main"))
    else:
        records = database.get_records()
        categories = database.get_categories()
        return render_template("index.html", rows=records, categories=categories)

if __name__ == "__main__":
    app.run(debug=True)