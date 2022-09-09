from Graph import *

import random
import sys

class ISPNetwork:

    def __init__(self):
        self.network = Graph()
        self.MST = Graph()

    def buildGraph(self, filename):
        with open(filename) as b:   #open the file using this function  
            for line in b:      #search each line in the file
                line = line.split(",")  #to separate using ,
                self.network.addEdge(line[0],line[1],float(line[2]))    #adding edges to the graph
        

    def pathExist(self, router1, route2):
        router1 = self.network.getVertex(router1)
        route2 = self.network.getVertex(route2)
        list = []   #list of vertices to be visited
        seen = []   #vertices that have already been visited
        list.append(router1)
        if router1 is None or route2 is None:   #if either routes are not in the graph
            return False
        if router1 == route2:   #if both routes are the same means that no path exists
            return True
        
        while len(list)>0:
            x = list.pop(0)
            seen.append(x)  #first vertex is always visited since we start there, thus we can count it as seen vertex
            for i in x.getConnections():    #for all neighbors of selected first vertex
                if i == route2:
                    return True
                else:
                    if i not in seen:   #if neighbor hasn't been visited already, append it to list which has vertices to be explored
                        list.append(i)
        return False    #if unable to find path

    def prim(self, graph, start):   #Prim's algorithm code from class lectures
        pq = PriorityQueue()
        for v in graph:
            v.setDistance(sys.maxsize)
            v.setPred(None)
        start.setDistance(0)
        pq.buildHeap([(v.getDistance(), v) for v in graph])
        while not pq.isEmpty():
            currentVert = pq.delMin()  
            for nextVert in currentVert.getConnections():  
                newCost = currentVert.getWeight(nextVert)
                if nextVert in pq and newCost < nextVert.getDistance():
                    nextVert.setPred(currentVert)
                    nextVert.setDistance(newCost)
                    pq.decreaseKey(nextVert, newCost)

    def buildMST(self):
        self.MST = Graph()  #initiate a graph for the MST
        t = self.network    
        i = [*t.getVertices()]  #store all the vertices kept in t 
        self.prim(t,t.getVertex(i[0]))
        for vertex in t:
            for nbr in vertex.getConnections(): #for each neighbor of the vertex 
                if nbr.getPred() == vertex: #if neighbor is predecessor of neighbor
                    self.MST.addEdge(nbr.getId(), vertex.getId(), vertex.getWeight(nbr))    #add edges to the MST
                    self.MST.addEdge(vertex.getId(), nbr.getId(), vertex.getWeight(nbr))
        

    def dijkstra(self, aGraph, start):  #Dijkstra's Algorithm code from class lectures
        pq = PriorityQueue()
        start.setDistance(0)
        pq.buildHeap([(v.getDistance(),v) for v in aGraph])
        while not pq.isEmpty():
            currentVert = pq.delMin()
            for nextVert in currentVert.getConnections():
                newDist = currentVert.getDistance() \
                        + currentVert.getWeight(nextVert)
                if newDist < nextVert.getDistance():
                    nextVert.setDistance( newDist )
                    nextVert.setPred(currentVert)
                    pq.decreaseKey(nextVert,newDist)


    def findPath(self, router1, router2):
        list = []
        path = ''
        route1 = self.MST.getVertex(router1)
        if self.MST is not None and route1 is not None: #if route1 and MST exist then run dijkstra algorithm
            self.dijkstra(self.MST, route1)

        route2 = self.MST.getVertex(router2)
        while route2 is not None and route2.getPred() is not None and route2.getId() != router1:    #while route2 is in MST and has a predecessor
            list.append(route2.getId())
            route2=route2.getPred()
        if route2 is not None:  #when route2 is in MST then add it to the path
            list.append(route2.getId())
        if router1 in list:     #if route1 is in the travelled list
            list.reverse()
            for r in list:
                if r != router2:    #if router in path is not the same as router2
                    path = path + r + ' -> '
                else:   #if router is the same
                    path = path + r
        else:       #if not in the travelled list
            path = 'path not exist'

        if self.MST is not None:    #resetting the MST
            for i in self.MST:
                if i is not None:
                    i.setDistance(sys.maxsize)
                    i.setPred(None)

        return path

    def findForwardingPath(self, router1, router2):
        list = []
        path = ''
        w = 0   #hold weight
        route1 = self.network.getVertex(router1)
        if route1 is None:  #if router1 is not in network
            return "path not exist"
        else:   #if in network run dijkstra's algorithm
            self.dijkstra(self.network, route1)
        
        route2 = self.network.getVertex(router2)
        while route2 is not None and route2.getPred() is not None and route2.getId() != router1:    #while route2 is in MST and has predecessor 
            list.append(route2.getId())
            w += route2.getWeight(route2.getPred()) ## add weight of edge between router2 and predecessor
            route2 = route2.getPred()   #set route to its predecessor
        if route2 is not None:  #if route2 is in network
            list.append(route2.getId())
        if router1 in list: #if router1 is in path
            list.reverse()
            for r in list:  #for each router in path
                if r != router2:
                    path = path + r + ' -> '
                else:
                    path = path + r + ' (' + str(w) + ')'   #add the weight to the output as well
        else:
            path = 'path not exist'
        
        if self.network is not None:    #resetting the network
            for i in self.network:
                if i is not None:
                    i.setDistance(sys.maxsize)
                    i.setPred(None)
        return path

    def dijkstra2(self, aGraph, start): #Dijkstra's algorithm but changed to find max distance
        pq = PriorityQueue()
        start.setDistance(0)
        pq.buildHeap([(v.getDistance(), v) for v in aGraph])
        while not pq.isEmpty():
            currentVert = pq.delMin()
            for nextVert in currentVert.getConnections():   #for each neighbor of current vertex
                newDist = max(currentVert.getDistance(), currentVert.getWeight(nextVert))   #new distance is max of vertex's distance and the weight of edge
                if newDist < nextVert.getDistance() and nextVert.getPred() != currentVert and currentVert.getPred() != nextVert:
                    nextVert.setDistance(newDist)
                    nextVert.setPred(currentVert)
                    pq.decreaseKey(nextVert, newDist)

    def findPathMaxWeight(self, router1, router2):
        list = []   
        path = ''
        route1 = self.network.getVertex(router1)
        if self.network is not None and route1 is not None: #if route1 is in the network
            self.dijkstra2(self.network, route1)    #run dijkstra's algorithm starting on route1
        route2 = self.network.getVertex(router2)

        while route2 is not None and route2.getPred() is not None and route2.getId() != router1:    #when route2 is in the network and also has a predecesor 
            if route2.getPred() is not None: #if predecessor exists
                list.append(route2.getId())
                route2 = route2.getPred()
        if route2 is not None:  #if route2 is in the network
            list.append(route2.getId())
        list.reverse()  #reverse the list of travelled vertices
        if router1 in list and router2 in list: #if both routers are in the travelled list
            for r in list:
                if r != router2:
                    path = path + r + ' -> '
                else:
                    path = path + r
        else:
            path = 'path not exist'
        
        if self.network is not None:    #resetting the network
            for i in self.network:
                if i is not None:
                    i.setDistance(sys.maxsize)
                    i.setPred(None)

        return path
        

    @staticmethod
    def nodeEdgeWeight(v):
        return sum([w for w in v.connectedTo.values()])

    @staticmethod
    def totalEdgeWeight(g):
        return sum([ISPNetwork.nodeEdgeWeight(v) for v in g]) // 2


if __name__ == '__main__':
    print("--------- Task1 build graph ---------")
    # Note: You should try all six dataset. This is just a example using 1221.csv
    net = ISPNetwork()
    net.buildGraph('data/1221.csv')

    print("--------- Task2 check if path exists ---------")
    routers = [v.id for v in random.sample(list(net.network.vertList.values()), 5)]
    for i in range(4):
        print('Router1:', routers[i], ', Router2:', routers[i+1], 'path exist?:', net.pathExist(routers[i], routers[i+1]))

    print("--------- Task3 build MST ---------")
    net.buildMST()
    print('graph node size', net.MST.numVertices)
    print('graph total edge weights', net.totalEdgeWeight(net.MST))

    print("--------- Task4 find shortest path in MST ---------")
    for i in range(4):
        print(routers[i], routers[i+1], 'Path:', net.findPath(routers[i], routers[i+1]))

    print("--------- Task5 find shortest path in original graph ---------")
    for i in range(4):
        print(routers[i], routers[i+1], 'Path:', net.findForwardingPath(routers[i], routers[i+1]))

    print("--------- Task6 find path in LowestMaxWeightFirst algorithm ---------")
    for i in range(4):
        print(routers[i], routers[i+1], 'Path:', net.findPathMaxWeight(routers[i], routers[i+1]))
