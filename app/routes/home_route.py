from flask import Flask

def home_route(app: Flask):

    @app.post("/post")
    def create_post():
        from app.controllers.user_controller import create_post
        return create_post()

    @app.get("/posts")
    def read_posts():
        from app.controllers.user_controller import read_posts
        return read_posts()
    
    @app.get("/posts/<int:id>")
    def read_posts_by_id(id):
        from app.controllers.user_controller import read_posts_by_id
        return read_posts_by_id(id)

    @app.delete("/posts/<int:id>")
    def delete_post(id):
        from app.controllers.user_controller import delete_post
        return delete_post(id)
    
    @app.patch("/posts/<int:id>")
    def update_post(id):
        from app.controllers.user_controller import update_post
        return update_post(id)