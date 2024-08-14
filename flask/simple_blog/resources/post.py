from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import PostModel
from schemas import PostSchema, PostUpdateSchema

blp = Blueprint("post", __name__)


@blp.route("/posts/<string:post_id>")
class Post(MethodView):
    @blp.response(200, PostSchema)
    def get(self, post_id):
        post = PostModel.query.get_or_404(post_id)
        return post

    def delete(self, post_id):
        post = PostModel.query.get_or_404(post_id)

        db.session.delete(post)
        db.session.commit()

        return {"message": "Post deleted"}, 200

    @blp.arguments(PostUpdateSchema)
    @blp.response(201, PostSchema)
    def put(self, post_data, post_id):
        post = PostModel.query.get(post_id)

        if post:
            post.title = post_data["title"]
            post.comment = post_data["comment"]
        else:
            post = PostModel(**post, id=post_id)

        db.session.add(post)
        db.session.commit()

        return post


@blp.route("/posts")
class PostList(MethodView):
    @blp.response(200, PostSchema(many=True))
    def get(self):
        return PostModel.query.all()

    @blp.arguments(PostSchema)
    @blp.response(201, PostSchema)
    def post(self, post_data):
        post = PostModel(**post_data)

        try:
            db.session.add(post)
            db.session.commit()
        except SQLAlchemyError:
            abort(
                500,
                message="An error occurred creating the store."
            )

        return post
