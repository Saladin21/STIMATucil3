import math

class findPath:
    def __init__ (self, graph, matrix):
        self.graph = graph.copy()
        self.matrix = matrix.copy()
        self.node = list(graph.keys())

    def EucDist(self, s1, s2):
        # sumber : https://community.esri.com/t5/coordinate-reference-systems/distance-on-a-sphere-the-haversine-formula/ba-p/902128

        lat1 = self.graph[s1][0]
        lon1 = self.graph[s1][1]
        lat2 = self.graph[s2][0]
        lon2 = self.graph[s2][1]

        R = 6371000  # radius of Earth in meters
        phi_1 = math.radians(lat1)
        phi_2 = math.radians(lat2)

        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)

        a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2
        
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        meters = R * c  # output distance in meters

        meters = round(meters, 3)
        return meters

    def Astar(self, s1, s2):
        return self.Astarrec([[self.EucDist(s1, s2), [s1]]], s2)

    def Astarrec(self, listActive, simpulTujuan):
        print(listActive)
        if(len(listActive) == 0):
            return ["ga nyambung", [simpulTujuan]]
        else:
            element = listActive[0]
            if(element[1][-1] == simpulTujuan):
                return element
            else:
                new = self.generate(element, simpulTujuan)
                listActive.pop(0)
                listActive.extend(new)
                listActive.sort(key=self.bantuSort)
                return self.Astarrec(listActive, simpulTujuan)

    def generate(self, element, simpulTujuan):
        hasil = []
        g = self.jatot(element[1])
        x = self.node.index(element[1][-1])
        for i in range(len(self.node)):
            if(self.matrix[x][i] == 1):
                temp = element[1].copy()
                if self.node[i] not in temp:
                    temp.append(self.node[i])
                    hasil.append([g+self.EucDist(element[1][-1], self.node[i])+self.EucDist(self.node[i], simpulTujuan), temp])
        return hasil

    def jatot(self, l): # jarak total
        if(len(l) <= 1):
            return 0
        else:
            s = 0
            for i in range(1, len(l)):
                s += self.EucDist(l[i-1], l[i])
            return s

    def bantuSort(self, element): # ya... buat bantu sort bang
        return element[0]
