import flask

app = flask.Flask("big-scroller")

@app.route('/')
def index():
    return flask.render_template('index.html')