#!/bin/python3

import math
import os
import random
import re
import sys
import copy

#
# Complete the 'hospital' function below.
#
# The function is expected to return an INTEGER.
# The function accepts UNWEIGHTED_INTEGER_GRAPH city as parameter.
#

#
# For the unweighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i].
#
#


def hospital(c_nodes, c_from, c_to):
    graph = [[] for _ in range((c_nodes + 1))]
    edges = [0] * (c_nodes + 1)
    visited = [False] * (c_nodes + 1)
    visited_counted = [False] * (c_nodes + 1)
    answer = 0

    for j in range(len(c_from)):
        a, b = c_from[j], c_to[j]
        graph[a].append(b)
        graph[b].append(a)

    for j in range(1, c_nodes + 1):
        edges[j] = len(graph[j])

    for j in range(1, c_nodes + 1):
        if edges[j] == 1:
            visited[graph[j][0]] = True
    visited_counted = visited[:]
    answer += visited.count(True)

    for j in range(1, c_nodes + 1):
        if visited[j]:
            for node in graph[j]:
                visited_counted[node] = True
    visited = visited_counted[:]

    while visited.count(False) != 1:
        graph_tmp = [[] for _ in range((c_nodes + 1))]
        edges_tmp = [0] * (c_nodes + 1)
        for j in range(1, c_nodes + 1):
            if not visited[j]:
                tmp = 0
                if len(graph[j]) == 0:
                    visited[j] = True
                    continue
                for node in graph[j]:
                    if not visited[node]:
                        tmp += 1
                        graph_tmp[j].append(node)
                edges_tmp[j] = tmp

        for j in range(1, c_nodes + 1):
            if edges_tmp[j] == 1:
                if not visited[j]:
                    visited[graph_tmp[j][0]] = True

        answer += visited.count(True) - visited_counted.count(True)
        visited_counted = visited[:]
        for j in range(1, c_nodes + 1):
            if visited[j]:
                for node in graph_tmp[j]:
                    visited_counted[node] = True
        visited = visited_counted[:]
        graph = copy.deepcopy(graph_tmp)
        edges = copy.deepcopy(edges_tmp)
    return answer


# Write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    city_nodes, city_edges = map(int, input().rstrip().split())
    city_from = [0] * city_edges
    city_to = [0] * city_edges
    for i in range(city_edges):
        city_from[i], city_to[i] = map(int, input().rstrip().split())
    result = hospital(city_nodes, city_from, city_to)
    fptr.write(str(result) + '\n')
    fptr.close()
