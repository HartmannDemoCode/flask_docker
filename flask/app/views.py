from app import app

import os
import json
from flask import jsonify, render_template

with open('recipes.json','r') as jsonfile:
        diction = json.load(jsonfile)

@app.route("/")
def index():
    # Use os.getenv("key") to get environment variables
    return render_template('./index.html')

@app.route("/recipes")
def recipes():
    return jsonify(diction['recipes'])

@app.route("/recipe/<id>")
def recipe(id):
    try:
        return jsonify(diction['recipes'][id])
    except: 
        return jsonify({"code":400,"error":"no recipe exist with id: "+id}),400

@app.route('/<path:path>')
def catch_all(path):
    resp = {"code":400,"error":path+" is not a valid resource on this server"}
    return jsonify(resp), 400 # second value in returned tuple is the status code