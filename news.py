from flask import Blueprint, render_template

news = Blueprint("news", __name__)


@news.route("/news")
def news_page():
    import dbUtils

    db = dbUtils.dbUtils("firstweb_flask.db")
    sql = "select * from news"
    newslist = db.db_action(sql, 1)
    return render_template("news.html", data=newslist)


@news.route("/news/edit")
def newsedit_page():
    return "/news/edit"
