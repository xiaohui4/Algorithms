# -*- coding: utf-8 -*-

from collections import deque
import pdb
import sys
import threading
import collections

def Kosaraju_SCCs():
    G_node_adjacent_edge = []
    with open("SCC.txt") as f:
        for line in f:
            directed_edge = list(map(int, line.split()))
            while(len(G_node_adjacent_edge) < directed_edge[0]):
                G_node_adjacent_edge.append([])
            G_node_adjacent_edge[directed_edge[0] - 1].append(directed_edge[1] - 1)
    node_num = len(G_node_adjacent_edge)
    print("There are {} nodes. Check first 10 nodes'adjacent edges: {}".format(node_num, G_node_adjacent_edge[:10]))
    
    #DFS_Loop on Grev to compute magical ordering of nodes
    #pdb.set_trace()
    Grev_node_adjacent_edge = [[] for i in range(node_num)]
    for node_index, adjacent_edges in enumerate(G_node_adjacent_edge):
        for adjacent_edge in adjacent_edges:
            Grev_node_adjacent_edge[adjacent_edge].append(node_index)
    print("G_node_adjacent_edge: {}\nGrev_node_adjacent_edge: {}".format(G_node_adjacent_edge[:3], Grev_node_adjacent_edge[:3]))
    node_fvalue = list(range(node_num))
    node_source = [None] * node_num
    print("="*10 + "Start assign magical f_value ordering to G_rev" + "=" * 10)
    DFS_Loop(Grev_node_adjacent_edge, node_fvalue, node_source) #node_fvalue return magical ordering of nodes
    print("Finish assign magical f_value ordering.\n")
    
    #DFS_Loop on G to discover the SCCs one by one
    node_source = [None] * node_num
    print("=" * 10 + "Start assign f_value to G" + "=" * 10)
    DFS_Loop(G_node_adjacent_edge, node_fvalue, node_source) #node_source return SCC's source node
    print("Finish assign nodes ordering.\n")
    #pdb.set_trace()
    SCC_list = collections.Counter(node_source).most_common(5)
    print(SCC_list) 

def DFS_Loop(node_adjacent_edge: list, node_fvalue: list, node_source: list):
    node_explore_list = [False] * len(node_adjacent_edge)
    current_fvalue = [len(node_adjacent_edge)]
    current_source = [None]

    #for-loop in increasing order of node_fvalue, each element is node_index
    node_fvalue_temp = [(index, value) for index, value in enumerate(node_fvalue)]
    node_fvalue_temp.sort(key = lambda x:x[1])
    print("Fvalue list is: {} ...".format(node_fvalue[:20]))
    print("Sorted fvalue_temp list is:{} ...".format(node_fvalue_temp[:20]))
    #pdb.set_trace()
                             
    for vertex_info in node_fvalue_temp:
        vertex_index = vertex_info[0]
        if node_explore_list[vertex_index] is False:
            current_source[0] = vertex_index
            DFS_Recursive(node_explore_list, node_adjacent_edge, node_fvalue, node_source, current_fvalue, current_source, vertex_index)

def DFS_Recursive(node_explore: list, adjacent_edges: list, node_fvalue: list, node_source: list, \
                  current_fvalue: list, current_source: list, search_node: int):
    node_explore[search_node] = True
    node_source[search_node] = current_source[0]
    #print("Explore vertex: {} and its adjacent vertices are: {}.".format(search_node, adjacent_edges[search_node]))
    #print("Explore vertex: {} from source vertex: {}.".format(search_node, current_source[0]))
    for adjacent_vertex in adjacent_edges[search_node]:
        if node_explore[adjacent_vertex] is False:
            DFS_Recursive(node_explore, adjacent_edges, node_fvalue, node_source, current_fvalue, current_source, adjacent_vertex)
    #assign fvalue to search_node
    node_fvalue[search_node] = current_fvalue[0]
    if(current_fvalue[0] % 10000 == 0):
        print("Assign node:{} as f_value: {}".format(search_node, current_fvalue[0]))
    current_fvalue[0] = current_fvalue[0] - 1
    #print("Finish exploring vertices from {} to {}.".format(current_source[0], search_node))

if __name__ == "__main__":
    sys.setrecursionlimit(2**20)
    threading.stack_size(100000000)
    thread = threading.Thread(target = Kosaraju_SCCs)
    thread.start()
