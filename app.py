from flask import Flask, render_template, url_for, request, redirect, jsonify, send_file
from findPath import findPath
import json


app = Flask(__name__)

graph = {}
matrix = []
node = [""]
buatAstar = []



@app.route('/')
def home():
    while(graph):
        graph.popitem()
    while (matrix):
        matrix.pop(0)
    while (buatAstar):
        buatAstar.pop(0)
    while (len(node) > 1):
        node.pop(0)
    return render_template('base.html')

@app.route('/', methods = ['POST', 'GET'])
def uploadFile():
    uploaded_file = request.files.getlist('Fileinput')
    for file_to_upload in uploaded_file:
        content = file_to_upload.read().decode("utf-8")
        namafile = file_to_upload.filename
        if (namafile == "Matriks.txt"):
            tempmatrix = content.strip().split('\n')
            for isi in tempmatrix:
                tempisi = map(int, isi.split(' '))
                matrix.append(list(tempisi))
        elif(namafile == "Graph.txt"):
            location = content.strip().split('\n')
            for i in range(1, int(location[0])+1):
                temp = location[i].strip('\r').split(' ' , 2)
                graph[temp[2]] = [float(temp[0]), float(temp[1])]
                node.append(temp[2])
    return render_template('base.html')


@app.route('/map', methods = ['POST'])
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

    return render_template('addEdge.html', graph=graph, node=node)

@app.route('/question', methods =['POST'])
def question():
    return render_template('question.html', graph=graph, matrix=matrix, node=node)

@app.route('/answer', methods =['POST'])
def answer():
    fp = findPath(graph, matrix)

    hasil = fp.Astar(buatAstar[0], buatAstar[1])
    if(type(hasil[0]) != str):
        hasil[0] = round(hasil[0], 3)

    return render_template('answer.html', graph=graph, matrix=matrix, hasil = hasil, node=node)

#python route
@app.route('/this-route', methods=['GET', 'POST'])
def thisRoute():
    information = json.loads(request.data )
    graph[str(information[0])] = [information[1]["lat"], information[1]["lng"]]
    node.append(str(information[0]))
    #print(graph)
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
    return "1"


@app.route('/downloadGraph', methods = ['GET', 'POST'])
def downloadGraph():
    path = "files/Graph.txt"
    f = open(path, "w")
    f.write(str(len(graph)))
    f.write("\n")
    for key in graph:
        s = str(graph[key][0]) + " " + str(graph[key][0]) + " " + str(key)
        f.write(s)
        f.write("\n")
    f.close()
    return send_file(path, as_attachment=True)

@app.route('/downloadMatriks', methods = ['GET', 'POST'])
def downloadMatriks():
    path = "files/Matriks.txt"
    f = open(path, "w")
    for i in range (len(matrix)):
        for j in range (len(matrix)):
            f.write(str(matrix[i][j]))
            f.write(" ")
        f.write("\n")
    f.close()
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
