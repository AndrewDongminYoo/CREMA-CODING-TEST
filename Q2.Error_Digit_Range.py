#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findRange' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER num as parameter.
#
def find_max(num):
    # 첫번째 숫자가 9가 아니라면 9로 바꾸면 간단하다.
    convert_target_index = -1
    for i in range(len(num)):
        if num[i] != '9':
            convert_target_index = i
            break
    converted_num = num.replace(num[convert_target_index], '9')
    return int(converted_num)


def find_min(num):
    # 두가지의 경우가 있을 수 있다..
    # 1. 첫번째 숫자가 1이 아닌 경우 (0일 수는 없으므로):
    #   - 첫번째 숫자를 1로 바꾼다..
    # 2. 첫번째 자리 숫자가 이미 1인 경우:
    #   - 두번째 자리의 숫자를 기준으로 1이 아닌 경우 0으로 교체한다.
    if num[0] != '1':
        return int(num.replace(num[0], '1'))
    else:
        convert_target_index = -1
        for i in range(1, len(num)):
            if num[i] != '0' and num[i] != num[0]:
                convert_target_index = i
                break
            elif i == len(num) - 1:
                return int(num.replace(num[0], '1'))
        converted_num = num.replace(num[convert_target_index], '0')
        return int(converted_num)


def find_range(num):
    # Write your code here
    if num < 10:  # 1자리 숫자인 경우
        return 8;
    stringify_num = str(num)
    maximum = find_max(stringify_num)
    minimum = find_min(stringify_num)
    return maximum - minimum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    num = int(input().strip())
    result = find_range(num)
    fptr.write(str(result) + '\n')
    fptr.close()
