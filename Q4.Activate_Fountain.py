#!/bin/python3

import os

# Complete the 'fountainActivation' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY locations as parameter.


def fountainActivation(location_points):
    # 정답 초기화
    fountain_cnt = 0
    # 화단의 길이
    length = len(location_points)
    # DP 배열 초기화
    dp = [-1] * length

    for i in range(length):
        min_index = max(i - location_points[i], 0)
        max_index = min(i + (location_points[i] + 1), length)
        dp[min_index] = max(dp[min_index], max_index)

    switch_on_index = 0
    each_end_index = dp[0]

    for i in range(len(dp)):
        if switch_on_index < dp[i]:
            switch_on_index = dp[i]

        # i 가 끝 index 에 다다르면, fountain_cnt 1 추가
        if i == each_end_index:
            fountain_cnt += 1
            each_end_index = switch_on_index

    return fountain_cnt + 1


if __name__ == '__main__':
    locations_count = int(input().strip())

    locations = []

    for _ in range(locations_count):
        point = int(input().strip())
        locations.append(point)

    result = fountainActivation(locations)

    print(str(result) + '\n')
