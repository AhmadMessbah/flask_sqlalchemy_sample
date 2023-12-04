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

@app.route("/user", methods=["GET"])
def user_list():
    for user in UserService.find_all():
        print(user.name)
    return render_template("user.html", users=UserService.find_all())
    # return UserService.find_all()


@app.route("/user/<int:id>/")
def user_id(id):
    user = UserService.find_by_id(id)
    if user:
        return user.json()
    return "Nooooooo", 403


if __name__ == "__main__":
    app.debug(True)
    app.run()
