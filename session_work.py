import imghdr

from flask import Flask, request, render_template, session, make_response

from controller.user_controller import UserController
from flask_session import Session
from model.service.user_service import UserService

UPLOAD_FOLDER = "./static/attach/"
ALLOWED_EXTENSIONS = set(["txt", "pdf", "png", "jpg", "jpeg", "gif"])

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

SESSION_PERMANENT = 30
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

@app.route("/login")
def login():
    # request.form.get("username")
    # request.form.get("password")
    session["username"] = "ali"
@app.route("/panel")
def panel():
    if session.get("username"):
        print("Welcome")
        return render_template("panel.html")
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.debug(True)
    app.run()
