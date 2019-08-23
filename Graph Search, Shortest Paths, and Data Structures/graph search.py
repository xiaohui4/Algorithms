# -*- coding: utf-8 -*-

from collections import deque
import pdb

def BFS(node_explore_list: list, adjacent_edge_list: list, start_node: int):
    node_queue = deque()
    node_queue.append(start_node)
    while(node_queue):
        node_popleft = node_queue.popleft()
        node_explore_list[node_popleft] = True
        print("Explore vertex: {}".format(node_popleft))
        for adjacent_vertex in adjacent_edge_list[node_popleft]:
            if node_explore_list[adjacent_vertex] is False:
                node_explore_list[adjacent_vertex] = True
                print("Mark {}'s adjacent vertex:{} as explored.".format(node_popleft, adjacent_vertex))
                node_queue.append(adjacent_vertex)

def DFS_Iterative(node_explore_list: list, adjacent_edge_list: list, start_node: int):
    node_stack = [start_node]
    while(node_stack):
        #pdb.set_trace()
        print(node_stack)
        node_pop = node_stack.pop()
        if node_explore_list[node_pop] is False:
            node_explore_list[node_pop] = True
            print("Explore vertex:{} and mark it as explored".format(node_pop))
            for adjacent_vertex in adjacent_edge_list[node_pop]:
                node_stack.append(adjacent_vertex)

def DFS_Recursive(node_explore_list: list, adjacent_edge_list: list, search_node: int):
    node_explore_list[search_node] = True
    print("Explore vertex: {}.".format(search_node))
    print("The current nodes of exploring is: {}".format(node_explore_list))
    for adjacent_vertex in adjacent_edge_list[search_node]:
        if node_explore_list[adjacent_vertex] is False:
            DFS_Recursive(node_explore_list, adjacent_edge_list, adjacent_vertex)

if __name__ == "__main__":
    print("=" * 30 + "  BFS version  " + "=" * 30)
    node_list = [False] * 7
    adjacent_edge_list = [[1, 2, 6], [0, 3], [0, 3], [1, 2, 4, 5], [2, 3, 5], [3, 4], [0]]
    BFS(node_list, adjacent_edge_list, 0)
    
    print("=" * 30 + "  DFS_Recursive version  " + "=" * 30)
    node_list = [False] * 7
    adjacent_edge_list = [[1, 2, 6], [0, 3], [0, 3], [1, 2, 4, 5], [2, 3, 5], [3, 4], [0]]
    DFS_Recursive(node_list, adjacent_edge_list, 0)

    print("=" * 30 + "  DFS_Iterative version  " + "=" * 30)
    node_list = [False] * 7
    adjacent_edge_list = [[1, 2, 6], [0, 3], [0, 3], [1, 2, 4, 5], [2, 3, 5], [3, 4], [0]]
    DFS_Iterative(node_list, adjacent_edge_list, 0)
