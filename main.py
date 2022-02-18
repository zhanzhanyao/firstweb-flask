from flask import Flask, render_template, url_for, request, redirect, session
from news import news
from user import user
from product import product

app = Flask(__name__)
app.secret_key = "password"
urls = [news, user, product]
for url in urls:
    app.register_blueprint(url)


@app.route("/")
def index():
    userinfo = ""
    return render_template("index.html", data=userinfo)


if __name__ == "__main__":
    print(app.url_map)
    app.run(host="127.0.0.1", port=2020, debug=True)
