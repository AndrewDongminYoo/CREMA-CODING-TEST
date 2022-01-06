#!/bin/python3

import math
import os
import random
import re
import sys


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
    return

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
