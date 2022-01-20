from flask import request, jsonify
from app import db
from app.models.classes.post import Post
from datetime import datetime

def create_post():
    data = request.get_json()
    id = len(list(db.posts.find()))+1
    title = data.get('title')
    author = data.get('author')
    tags = data.get('tags')
    content = data.get('content')
    if title == None or author == None or tags == None or content == None:
        return {"wrong fields": [{"title": type(title).__name__, "author": type(author).__name__, "tags": type(tags).__name__, "content": type(content).__name__}]}, 400
    new_data = Post(id, title, author, tags, content)
    post_data = new_data.__dict__
    db.posts.insert_one(post_data)
    del post_data["_id"]
    return post_data, 201

def read_posts():
    all_posts = list(db.posts.find())
    for post in all_posts:
        del post["_id"]
    return jsonify(all_posts), 200

def read_posts_by_id(id):
    all_posts = list(db.posts.find())
    for post in all_posts:
        del post["_id"]
        if post["id"] == id:
            return post, 200
    return {"message": "id não existente no banco"}, 404

def delete_post(id):
    try:
        deleted = db.posts.find_one({'id': int(id)})
        del deleted["_id"]
        db.posts.delete_one({"id": int(id)})
        return deleted, 200
    except TypeError:
        return {"message": "post inexistente"}, 404

def update_post(id):
    try:
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')
        tags = data.get('tags')
        content = data.get('content')
        if title == None and author == None and tags == None and content == None:
            return {"message": "JSON inválido"}, 400
        db.posts.update_one({"id": int(id)}, {"$set": {**data, "updated_at": datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")}} )
        updated = db.posts.find_one({'id': int(id)})
        del updated['_id']
        return updated, 200
    except TypeError:
        return {"message": "id não existente no banco"}, 404