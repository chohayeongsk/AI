from flask import Blueprint, render_template
crud = Blueprint( # 이름 정의
    "crud",
    __name__,
    template_folder="templates", #html
    static_folder="static", #css
)
@crud.route("/")
def index():
    return render_template("crud/index.html")