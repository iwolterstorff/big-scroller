import json
import os

import flask
import pymongo
mongo_url = os.getenv('MONGODB_URI')
db = pymongo.MongoClient(mongo_url, retryWrites=False).get_database()
collection = db.phrases

def get_phrases():
    return [item['phrase'] for item in list(collection.find({}, {"_id": 0}))]

app = flask.Flask("big-scroller")

@app.route('/')
def index():
    return flask.render_template('index.html', phrases=json.dumps(get_phrases()))

@app.route('/update', methods=['GET', 'POST'])
def update():
    if flask.request.method == "GET":
        return flask.render_template('update.html')
    else:
        new_phrase = flask.request.form.get('phrase')
        collection.insert_one({"phrase": new_phrase})
        return flask.redirect('/')