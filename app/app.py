from flask import Flask, render_template

app = Flask(__name__)

# ---------------------------
# Login Page
# ---------------------------
@app.route("/")
def login():
    return render_template("login.html")


# ---------------------------
# Artisan Dashboard
# ---------------------------
@app.route("/artisan")
def artisan():
    return render_template("artisan.html")


# ---------------------------
# Curator Dashboard
# ---------------------------
@app.route("/curator")
def curator():
    return render_template("curator.html")


# ---------------------------
# Run Server
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)
