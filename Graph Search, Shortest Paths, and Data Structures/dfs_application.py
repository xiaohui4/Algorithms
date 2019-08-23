# -*- coding: utf-8 -*-

from collections import deque
import pdb

def DFS_Recursive(node_explore_list: list, adjacent_edge_list: list, node_fvalue_list: list, current_label: list, search_node: int):
    node_explore_list[search_node] = True
    print("Explore vertex: {}.".format(search_node))
    print("The current nodes of exploring is: {}".format(node_explore_list))
    for adjacent_vertex in adjacent_edge_list[search_node]:
        if node_explore_list[adjacent_vertex] is False:
            DFS_Recursive(node_explore_list, adjacent_edge_list, node_fvalue_list, current_label, adjacent_vertex)
    node_fvalue_list[search_node] = current_label[0]
    current_label[0] = current_label[0] - 1

def DFS_Loop(node_explore_list: list, adjacent_edge_list: list, node_fvalue_list: list):
    current_label = [len(node_explore_list)]
    for vertex_index in range(len(node_explore_list)):
        if node_explore_list[vertex_index] is False:
            DFS_Recursive(node_explore_list, adjacent_edge_list, node_fvalue_list, current_label, vertex_index)

if __name__ == "__main__":
    print("=" * 30 + "  DFS_Loop(Topological Sort)  " + "=" * 30)
    node_list = [False] * 7
    node_list_value = [False] * 7
    adjacent_edge_list = [[1, 2], [4], [3, 4], [6], [5], [], []]
    DFS_Loop(node_list, adjacent_edge_list, node_list_value)
    print(node_list_value)
