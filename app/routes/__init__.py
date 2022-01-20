from flask import Flask

def init_app(app: Flask):
    from app.routes.home_route import home_route
    home_route(app)