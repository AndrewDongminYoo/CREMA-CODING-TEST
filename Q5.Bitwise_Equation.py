#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'bitwiseEquations' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER_ARRAY b
#

# 비트연산자
# & AND A와 B 둘 다 참이다.
# | OR A와 B 중 하나 이상 참이다.
# ^ XOR A와 B 중 하나만 참이다.
# ~ NOT A가 아니다. (1항 연산자)
# << 왼쪽으로 B 만큼 이동 (1<<3 -> 8)
# >> 오른쪽쪽으로 B 만큼 이동 (8>>2 -> 2)

def bitwise_equations(array1, array2):

    def get_bit_result(expected_add_result, expected_bit_xor_result):
        # expected_bit_xor_result = 2, expected_add_result = 4
        # A = 1
        A = (expected_add_result - expected_bit_xor_result) // 2
        x = 0
        y = 0
        for n in range(40):  # n = 0 ? Xi = 0, Ai = 1
            Xi = (expected_bit_xor_result & (1 << n))
            Ai = (A & (1 << n))
            if x + y == expected_add_result and x ^ y == expected_bit_xor_result:
                break
            if Xi == 0 and Ai == 0:
                pass
            elif Xi == 0 and Ai > 0:
                x = ((1 << n) | x)  # 1
                y = ((1 << n) | y)  # 1

            elif Xi > 0 and Ai == 0:
                y = ((1 << n) | y)
            else:
                return 0

        return 2 * x + 3 * y  # 11

    answer = []

    for i in range(len(array1)):
        answer.append(get_bit_result(array1[i], array2[i]))

    return answer


if __name__ == '__main__':

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    b_count = int(input().strip())

    b = []

    for _ in range(b_count):
        b_item = int(input().strip())
        b.append(b_item)

    result = bitwise_equations(a, b)

    print('\n'.join(map(str, result)))
