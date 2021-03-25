import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/whyliverpool')
def whyliverpool():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("whyliverpool.html", page_title="Why Liverpool", company=data)


@app.route('/whyliverpool/<member_name>')
def whyliverpool_member(member_name):
    member = {}

    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj 
    return render_template("member.html", member=member)

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message".format(
            request.form["name"]
        ))
    return render_template("contact.html", page_title="Contact")


@app.route('/property')
def property():
    return render_template("property.html", page_title="Property")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get("PORT", "8000")),
            debug=True)