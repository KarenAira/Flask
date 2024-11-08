from flask import Flask, make_response
from pymongo import MongoClient

def make_app(mongodb_uri):
    app = Flask("my app")
    db = MongoClient(mongodb_uri)

    @app.route("/pages/<page_name>")
    def page(page_name):
        doc = db.content.pages.find_one({'name': page_name})
        return make_response(doc['contents'])

    return app