from flask import Blueprint, render_template

product = Blueprint("product", __name__)


@product.route("/product")
def product_page():
    return render_template("product.html")
