#!/bin/python3

import collections

#
# Complete the 'countMatches' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid1
#  2. STRING_ARRAY grid2


def BFS(y, x, grid1, visited):
    # Define directions.
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)];

    # bfs results. - saves indexes which value is 1.
    bfs_results = [[y, x]];

    # deque, that will be using in BFS.
    deq = collections.deque();
    # first, append (y, x) in deq.
    deq.append((y, x));
    while deq:
        target_y, target_x = deq.popleft();
        for direction in dirs:
            new_y, new_x = target_y + direction[0], target_x + direction[1];
            if 0 <= new_y < len(grid1) and 0 <= new_x < len(grid1[0]) and visited[new_y][new_x] == 0:
                if grid1[new_y][new_x] == 1:
                    deq.append((new_y, new_x));
                    visited[new_y][new_x] = 1;
                    bfs_results.append((new_y, new_x));
    return bfs_results;


def count_matches(grid_data1, grid_data2):
    answer = 0

    visited_grid1 = []
    for y in range(len(grid_data1)):
        temp = [0] * len(grid_data1[0])
        visited_grid1.append(temp)

    visited_grid2 = []
    for y in range(len(grid_data2)):
        temp = [0] * len(grid_data2[0])
        visited_grid2.append(temp)

    for y in range(len(grid_data1)):
        for x in range(len(grid_data1[0])):
            if grid_data1[y][x] == 1:
                if grid_data2[y][x] == 1:
                    if visited_grid1[y][x] == 0:
                        if visited_grid2[y][x] == 0:
                            visited_grid1[y][x] = 1
                            visited_grid2[y][x] = 1
                            grid1_bfs_result = BFS(y, x, grid_data1, visited_grid1)
                            grid2_bfs_result = BFS(y, x, grid_data2, visited_grid2)

                            print(grid1_bfs_result)
                            print(grid2_bfs_result)
                            if grid1_bfs_result == grid2_bfs_result:
                                answer += 1

                            grid1_bfs_result.clear()
                            grid2_bfs_result.clear()
    return answer


if __name__ == '__main__':
    grid1 = ['0100', '1001', '0011', '0011']
    grid2 = ['0101', '1001', '0011', '0011']
    grid1_item_list = []
    grid2_item_list = []
    for _ in range(4):
        grid1_item = list(map(int, list(grid1[_])))
        grid1_item_list.append(grid1_item)
        grid2_item = list(map(int, list(grid2[_])))
        grid2_item_list.append(grid2_item)
    result = count_matches(grid1_item_list, grid2_item_list)
    print(result)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     grid1_count = int(input().strip())
#
#     grid1 = []
#     for _ in range(grid1_count):
#         grid1_item = list(map(int, list(input())))
#         grid1.append(grid1_item)
#     grid2_count = int(input().strip())
#
#     grid2 = []
#     for _ in range(grid2_count):
#         grid2_item = list(map(int, list(input())))
#         grid2.append(grid2_item)
#
#     result = count_matches(grid1, grid2)
#     fptr.write(str(result) + '\n')
#     fptr.close()
