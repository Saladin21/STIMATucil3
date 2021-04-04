from flask import Flask, render_template, url_for, request, redirect, jsonify
from findPath import findPath
import json


app = Flask(__name__)

graph = {}
matrix = []




@app.route('/')
def index():
    return render_template('home.html')

#python route
@app.route('/this-route', methods=['GET', 'POST'])
def thisRoute():
    information = json.loads(request.data )
    graph[information[0]] = [information[1]["lat"], information[1]["lng"]]
    //print(graph)
    return "1"

if __name__ == "__main__":
    app.run(debug=True)
