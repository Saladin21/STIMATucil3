
def EucDist(s1, s2):
    x1 = graph[s1][0]; y1 = graph[s1][1]
    x2 = graph[s2][0]; y2 = graph[s2][1]
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

def Astar(s1, s2):
    return Astarrec([[EucDist(s1, s2), [s1]]], s2)

def Astarrec(listActive, simpulTujuan):
    print(listActive)
    if(len(listActive) == 0):
        return "ga nyambung"
    else:
        element = listActive[0]
        if(element[1][-1] == simpulTujuan):
            return element
        else:
            new = generate(element, simpulTujuan)
            listActive.pop(0)
            listActive.extend(new)
            listActive.sort(key=bantuSort)
            return Astarrec(listActive, simpulTujuan)

def generate(element, simpulTujuan):
    hasil = []
    g = jatot(element[1])
    x = node.index(element[1][-1])
    for i in range(len(node)):
        if(matrix[x][i] == '1'):
            temp = element[1].copy()
            temp.append(node[i])
            hasil.append([g+EucDist(element[1][-1], node[i])+EucDist(node[i], simpulTujuan), temp])
    return hasil

def jatot(l): # jarak total
    if(len(l) <= 1):
        return 0
    else:
        s = 0
        for i in range(1, len(l)):
            s += EucDist(l[i-1], l[i])
        return s

def bantuSort(element): # ya... buat bantu sort bang
    return element[0]

# buka dan simpan lokasi setiap node
with open("location.txt") as f:
    location = f.read().strip().split('\n')

graph = {}
for i in range(1, len(location)):
    temp = location[i].split(' ')
    graph[temp[0]] = [float(temp[1]), float(temp[2])]
node = list(graph.keys())

#buka dan simpan matriks sisi
with open("matrix.txt") as f:
    tempmatrix = f.read().strip().split('\n')
matrix = []
for isi in tempmatrix:
    matrix.append(isi.split(' '))
print(matrix)

# program utama
end = False
while(not(end)):
    i = 1
    for j in graph:
        print(f"{i}. {j}")
        i += 1
    simpul1 = input()
    simpul1 = "titik1"
    while not(simpul1 in graph):
        simpul1 = input()
    simpul2 = input()
    simpul2 = "titik3"
    while not(simpul2 in graph):
        simpul2 = input()
    jalur = Astar(simpul1, simpul2)
    print(jalur)
    end = True