from flask import Flask
from datetime import datetime
import flask
import pymongo

app = Flask(__name__)
db = pymongo.MongoClient(host="mongo").containers

@app.route('/')
def index():
  return "Hello world!"

@app.route('/containers')
def containers():
  return flask.json.dumps([{"name": e["name"] } for e in list(db.Containers.find())])

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80, debug=True)
