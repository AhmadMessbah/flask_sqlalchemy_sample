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

@app.route("/")
def login():
    # print(request.cookies.get("username"))
    # print(request.cookies.get("password"))
    # print(request.cookies.get("color"))
    return render_template("cookie.html",
                           username = request.cookies.get("username"),
                           password = request.cookies.get("password"),
                           color=request.cookies.get("color"))

    # write cookie
    # response = make_response(render_template("login.html"))
    # response.set_cookie("username", value="ali")
    # response.set_cookie("password", value="ali123")
    # response.set_cookie("color", value="red")
    #
    # return response


if __name__ == "__main__":
    app.debug(True)
    app.run()
