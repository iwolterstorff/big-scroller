import os

import flask
import pymongo

mongo_url = os.getenv('MONGODB_URI')
client = pymongo.MongoClient(mongo_url)
db = client.database
collection = db.phrases

app = flask.Flask("big-scroller")

@app.route('/')
def index():
    return flask.render_template('index.html')