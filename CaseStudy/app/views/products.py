from flask import render_template, Blueprint, request
from app.controllers import GetProductList, CreateAddingRequest, GetProductByID

bp = Blueprint("products", __name__, template_folder="../templates")


@bp.route("/", methods=["GET", "POST"])
def Index():
    productList = GetProductList()
    return render_template("productList.html", productList = productList)



@bp.route("/product-add", methods=["GET", "POST"])
def AddProduct():
    display = "none"
    if request.method == "POST":
        if request.form:
            productID = request.form.get("productID")
            productName = request.form.get("productName")
            productDescription = request.form.get("productDescription")
            productImageURL = request.form.get("productImageURL")
            productReleaseDate = request.form.get("productReleaseDate")
            productPrice = request.form.get("productPrice")
            CreateAddingRequest(productID,
                              productName,
                              productDescription,
                              productImageURL,
                              productReleaseDate,
                              productPrice)
            display = "block"
    return render_template("addProduct.html", display= display)


@bp.route("/product", methods=["GET", "POST"])
def Product():
    if request.method == "POST":
        if request.form:
            productID = request.form.get("productID")
            product = GetProductByID(productID)
            return render_template("product.html", product=product)
    return render_template("product.html")