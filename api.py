from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'hotel'
app.config['MONGO_URI'] = 'mongodb://hotel:paopao00@ds259144.mlab.com:59144/hotel'

mongo = PyMongo(app)

@app.route('/hotel', methods=['GET'])
def get_all_stars():
  star = mongo.db.customers
  output = []
  for s in star.find():
    output.append({'link' : s['name'], 'Hotel' : s['address'] })
  return jsonify({'result' : output})

@app.route('/hotel/<sighting_id>', methods=['GET'])
def get_one_star(sighting_id):
  star = mongo.db.customers
  s = star.find_one({'_id': ObjectId(sighting_id)})
  if s:
    output = {'link' : s['name'], 'Hotel' : s['address']}
  else:
    output = "No such name"
  return jsonify({'result' : output})



if __name__ == '__main__':
    app.run(debug=True)

