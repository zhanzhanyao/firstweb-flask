from flask import Blueprint, render_template, session, url_for, request
from werkzeug.utils import redirect

user = Blueprint("user", __name__)  # 蓝图使用方法， 参数里给定文件名，还可以给出url前缀


@user.route("/login")  # 使用user的路由配置
def login_page():
    return render_template("login.html")


@user.route("/loginProcess", methods=["POST,GET"])
def loginprocess_page():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        if name == "cao" and password == "123":
            session["username"] = name
            print(session["username"])
            return redirect(url_for("index"))
        else:
            return "the username or password does not match"
