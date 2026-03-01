#Test Run

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/artisan")
def artisan():
    return render_template("artisan.html")

@app.route("/curator")
def curator():
    return render_template("curator.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
