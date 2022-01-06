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
# & AND
# | OR
# ^ XOR
# ~ NOT

def bitwise_equations(array1, array2):
    N = len(a)
    answer = []

    def get_bit_result(expected_add_result: int, expected_bit_xor_result: int) -> int:
        # expected_add_result = 4 expected_bit_xor_result = 2
        # A = 1
        A = (expected_add_result - expected_bit_xor_result) // 2
        x = 0
        y = 0
        for n in range(40):
            Xi = (expected_bit_xor_result & (1 << n))  # 2 & 10  == 10
            Ai = (A & (1 << n))  # 1 & 10 == 0
            if x + y == expected_add_result and x ^ y == expected_bit_xor_result:
                break
            if Xi == 0 and Ai == 0:
                pass
            elif Xi == 0 and Ai > 0:
                x = ((1 << n) | x)  # 1
                y = ((1 << n) | y)  # 1

            elif Xi > 0 and Ai == 0:
                y = ((1 << n) | y)  # 11
            else:
                return 0

        return 2 * x + 3 * y

    for i in range(N):
        answer.append(get_bit_result(array1[i], array2[i]))

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

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

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
