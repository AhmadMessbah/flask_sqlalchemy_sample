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
            file.save(UPLOAD_FOLDER + file.filename)

    return render_template("user.html", user=user)


if __name__ == "__main__":
    app.debug(True)
    app.run()
