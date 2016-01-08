# Students: please do not edit this file.

import json
import requests
import os
from flask import Flask, request, render_template
from search import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("search.html")

@app.route("/search", methods = ["GET", "POST"])
def search_handler():
    if request.method == "POST":
        query = request.args.get('search')
        results = search(query)
        return results
        
    else:
        return render_template("search.html")

@app.route("/search_raw", methods = ["POST"])
def search_raw():
    query = request.form["query"]
    results = search(query)
    return results

if __name__ == "__main__":
    app.run(host = os.getenv('IP', '0.0.0.0'), port = int(os.getenv('PORT', 8080)), debug=True)