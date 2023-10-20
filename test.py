import math
import os
import random
import re
import sys

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs_bf(k, arr): # O(n^2)
    num_of_pairs = 0
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if abs(arr[i] - arr[j]) == k:
                num_of_pairs += 1
    
    return num_of_pairs


def pairs(k, arr):
    values_histogram = {}
    for value in arr:
        values_histogram[value] = values_histogram.get(value, 0) + 1
    
    # for key, value in values_histogram.items():
    #     print(key, value)
    
    num_of_pairs = 0
    for value in arr:
        other_value = abs(k - value)
        if other_value in values_histogram:
            num_of_pairs += values_histogram[other_value]
            if other_value == value:
                num_of_pairs -= 1

    return num_of_pairs


if __name__ == '__main__':
    with open('testcase.txt', 'r') as file:
        line = file.readline().split()
        n, k = int(line[0]), int(line[1])
        line = file.readline().split()
        arr = list(map(int, line))

    result = pairs(k, arr)
    print(result)

# 46757