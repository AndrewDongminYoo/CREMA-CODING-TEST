#!/bin/python3

import os
import collections


#
# Complete the 'countMatches' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid1
#  2. STRING_ARRAY grid2
#

def bread_first_search(y, x, grid, visited):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 4 방향 정의

    bfs_results = [[y, x]]

    queue = collections.deque()
    queue.append((y, x))
    while queue:
        target_y, target_x = queue.popleft()
        for direction in directions:
            new_y, new_x = target_y + direction[0], target_x + direction[1]
            if 0 <= new_y < len(grid):
                if 0 <= new_x < len(grid[0]):
                    if visited[new_y][new_x] == 0:
                        if grid[new_y][new_x] == 1:
                            queue.append((new_y, new_x))
                            visited[new_y][new_x] = 1
                            bfs_results.append((new_y, new_x))
    return bfs_results


def count_matches(grid_a, grid_b):
    answer = 0

    visited_grid1 = []
    for y in range(len(grid_a)):
        temp = [0] * len(grid_a[0])
        visited_grid1.append(temp)

    visited_grid2 = []
    for y in range(len(grid_b)):
        temp = [0] * len(grid_b[0])
        visited_grid2.append(temp)

    for y in range(len(grid_a)):
        for x in range(len(grid_a[0])):
            if grid_a[y][x] == 1:  # 두 그리드의 칸이 차 있는지 확인
                if grid_b[y][x] == 1:
                    if visited_grid1[y][x] == 0:  # 방문한 칸인지 확인
                        if visited_grid2[y][x] == 0:
                            visited_grid1[y][x] = 1
                            visited_grid2[y][x] = 1
                            grid1_bfs_result = bread_first_search(y, x, grid_a, visited_grid1)
                            grid2_bfs_result = bread_first_search(y, x, grid_b, visited_grid2)

                            print(grid1_bfs_result)
                            print(grid2_bfs_result)
                            if grid1_bfs_result == grid2_bfs_result:
                                answer += 1

                            grid1_bfs_result.clear()  # deque 메소드
                            grid2_bfs_result.clear()

    return answer


if __name__ == '__main__':
    grid1_count = int(input().strip())

    grid1 = []

    for _ in range(grid1_count):
        grid1_item = list(map(int, list(input())))
        grid1.append(grid1_item)

    grid2_count = int(input().strip())

    grid2 = []

    for _ in range(grid2_count):
        grid2_item = list(map(int, list(input())))
        grid2.append(grid2_item)

    result = count_matches(grid1, grid2)

    print(str(result) + '\n')
