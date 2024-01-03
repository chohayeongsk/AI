from flask import Flask
def create_app() :
    app = Flask(__name__) 

    from apps.crud import views as crud_views #뷰에서 apps.crud 만듦 앱에서, 크루드 가져오기 / 

    app.register_blueprint(crud_views.crud, url_prefix = "/crud") #blueprint = 이름(식별), url = 식별자, crud 링크에 crud 이름 붙임. 

    return app


