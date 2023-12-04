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

phase = None


@app.route("/")
def home():
    session["username"] = "ahmad_user"
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    print(request.cookies.get("username"))
    if request.method == "POST":
        print(request.form.get("username"))
        print(request.form.get("password"))
        print(request.form.get("remember"))

        response = make_response(render_template("login.html"))
        response.set_cookie("username", value=request.form.get("username"))
        response.set_cookie("password", value=request.form.get("password"))

        return response

    return render_template("login.html",prediction="", show_predictions_modal=True)


@app.route("/user", methods=["GET", "POST"])
def user():
    print(session.get("user"))
    user = None
    if request.method == "POST":
        user = UserController.save(
            request.form.get("name"),
            request.form.get("family"),
            request.form.get("username"),
            request.form.get("password"),
        )
        file = request.files["file"]
        if imghdr.what(file):
            file.save(UPLOAD_FOLDER + "file." + imghdr.what(file))

    return render_template("user.html", user=user)


@app.route("/user/<int:id>/")
def user_id(id):
    user = UserService.find_by_id(id)
    if user:
        return user.json()
    return "", 204


if __name__ == "__main__":
    app.debug(True)
    app.run()
