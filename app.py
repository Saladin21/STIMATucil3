from flask import Flask, render_template, url_for, request, redirect, jsonify
from findPath import findPath
import json


app = Flask(__name__)

graph = {}
matrix = []
buatAstar = []




@app.route('/')
def index():
    while(graph):
        graph.popitem()
    return render_template('home.html')

@app.route('/sendGraph', methods =['POST'])
def sendGraph():
    while (matrix):
        matrix.pop(0)
    for j in range(len(graph)):
        matrix.append([0 for i in range(len(graph))])

    #print(matrix)
    return render_template('addEdge.html', graph=graph)

@app.route('/question', methods =['POST'])
def question():
    return render_template('question.html', graph=graph, matrix=matrix)

@app.route('/answer', methods =['POST'])
def answer():
    fp = findPath(graph, matrix)
    print(buatAstar)
    print(graph)
    print(matrix)
    hasil = fp.Astar(int(buatAstar[0]), int(buatAstar[1]))
    hasil[0] = round(hasil[0], 3)
    print(hasil)
    return render_template('answer.html', graph=graph, matrix=matrix, hasil = hasil)

#python route
@app.route('/this-route', methods=['GET', 'POST'])
def thisRoute():
    information = json.loads(request.data )
    graph[information[0]] = [information[1]["lat"], information[1]["lng"]]
    print(graph)
    return "1"

@app.route('/kirim_matriks', methods=['GET', 'POST'])
def dapetMatriks():
    info = json.loads(request.data)
    #print(info)
    #print(matrix)
    if (info[0] != info[1]):
        matrix[int(info[0])-1][int(info[1])-1] = 1
        matrix[int(info[1])-1][int(info[0])-1] = 1
    return "1"

@app.route('/kirim_simpul', methods=['GET', 'POST'])
def dapetSimpul():
    while (buatAstar):
        buatAstar.pop(0)
    info = json.loads(request.data)
    buatAstar.append(info[0])
    buatAstar.append(info[1])
    print(buatAstar)
    return "1"

if __name__ == "__main__":
    app.run(debug=True)
