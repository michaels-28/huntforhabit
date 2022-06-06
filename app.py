import os
from flask import(Flask, flash, render_template, redirect, request, session, url_for, Response)
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route("/")
def test():
    return render_template("base.html")

@app.route("/test2")
def test2():
    return render_template("luke.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/online_coaching")
def online_coaching():
    return render_template("online_coaching.html")

@app.route("/free_consultation")
def free_consultation():
    return render_template("free_consultation.html")

@app.route("/testimonials")
def testimonials():
    return render_template("testimonials.html")

@app.route("/calorie_calculator")
def calorie_calculator():
    return render_template("calorie_calculator.html")

@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")

@app.route("/log_in")
def log_in():
    return render_template("log_in.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/client_plan")
def client_plan():
    return render_template("client_plan.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
