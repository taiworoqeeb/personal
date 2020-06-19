from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Register", methods=["POST", "GET"])
def register():
    name = request.form.get("name")
    return render_template("Register.html", name=name)