# -*- coding: utf-8 -*-

import pdb
import sys
import random
import math
import copy

def kargerMinCut(graphDict: dict):
    #pdb.set_trace()
    edgeNum = 0
    if(len(graphDict) == 2):
        for key, value in graphDict.items():
            edgeNum += len(value)
        return edgeNum / 2
    else:
        #pick a remaining edge (u,v) uniformly at random
        (u, v) = pickEdge(graphDict)
        #merge/contract u and v into a single vertex
        #print("The graph is:{}. Pick the edge:{} and merge the two vertices.".format(graphDict, (u,v)))
        mergeVertices(graphDict, u, v)
        #print("After merging, the graph is: {}".format(graphDict))
        edgeNum = kargerMinCut(graphDict)
        return edgeNum
        #remove self-loops

def pickEdge(tempGraph: dict):
    edgeList = []
    for keyVertex, adjacentVerticesList in tempGraph.items():
        [edgeList.append((keyVertex, adjacentVertex)) for adjacentVertex in adjacentVerticesList]
    index = random.randint(0, len(edgeList)-1)
    #print("The selected edge is {}th of {} edges.".format(index, len(edgeList)))
    #pdb.set_trace()
    return edgeList[index]

def mergeVertices(graphDict: dict, u: tuple, v: tuple):
    #pdb.set_trace()
    uAdjacentVertices = graphDict[u]
    del graphDict[u]
    vAdjacentVertices = graphDict[v]
    del graphDict[v]
    uvAdjacentVertices = uAdjacentVertices + vAdjacentVertices #merge adjacent vertices of u and v
    uvKey = u + v
    graphDict[uvKey] = uvAdjacentVertices
    pattern = [u, v, u + v]
    for key, value in graphDict.items(): #replace ((u,) or (v,) by (u, v)
        graphDict[key] = [uvKey if adjacentVertex in pattern else adjacentVertex for adjacentVertex in value]
    while(uvKey in graphDict[uvKey]): #remove self-loops
        graphDict[uvKey].remove(uvKey)

if __name__ == '__main__':
    graphDict = {} # key is a tuple representing vertex, value is a list representing adjacent vertices
    test = False
    if(test == True):
        graphDict[(1,)] = [(2,), (3,)]
        graphDict[(2,)] = [(1,), (3,), (4,)]
        graphDict[(3,)] = [(1,), (2,), (4,)]
        graphDict[(4,)] = [(2,), (3,)]
    else:
        adjacentVerticesList = list()
        #pdb.set_trace()
        with open("kargerMinCut.txt") as f:
            for line in f:
                vertex_edges = list(map(int, line.split())) #list element string to int
                [adjacentVerticesList.append((vertex,)) for vertex in vertex_edges[1:]]
                graphDict[(vertex_edges[0],)] = adjacentVerticesList[:]
                adjacentVerticesList.clear()

    edgeNum = 0
    for key, value in graphDict.items():
        edgeNum += len(value)
    edgeNum = edgeNum / 2
    vertexNum = len(graphDict)
    print("There are {} vertices and {} edges in the graph.".format(vertexNum, edgeNum))
    minCutNum = vertexNum
    rounds = int(vertexNum * vertexNum * math.log(vertexNum))
    for i in range(rounds):
        #pdb.set_trace()
        graphDictIn = copy.deepcopy(graphDict)
        tempCutEdgeNum = kargerMinCut(graphDictIn)
        if(minCutNum > tempCutEdgeNum):
            minCutNum = tempCutEdgeNum
        print("In {}th round, the cut edge num is {}. The min cut edge num is {}".format(i, tempCutEdgeNum, minCutNum))
        if(i % 100 == 0):
            print("=" * 30 + "{}th rounds".format(i) + "=" * 30)
