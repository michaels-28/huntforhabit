import os
from flask import(Flask, flash, render_template, redirect, request, session, url_for, Response)
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

@app.route("/")
def test():
    return render_template("base.html")

@app.route("/test2")
def test2():
    return render_template("luke.html")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)