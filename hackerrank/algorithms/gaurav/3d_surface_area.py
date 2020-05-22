# https://www.hackerrank.com/challenges/3d-surface-area/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    H = len(A)
    W = len(A[0])
    total = 0
    for i in range(H):
        for j in range(W):

            left = (i, j-1)
            right = (i, j+1)
            up = (i-1, j)
            down = (i+1, j)

            temp = [left, right, up, down]
            adjacent = list()
            
            for cord in temp:
                x = cord[0]
                y = cord[1]
                if (x >= 0 and x < H) and (y >= 0 and y < W):
                    adjacent.append(cord)
                else:
                    pass
            
            height = A[i][j]
            
            adj_heights = list()

            for block in adjacent:
                adj_heights.append(A[block[0]][block[1]])

            area_threshold = ((4 - len(adjacent)) * height) + 2
            lst = list()

            for block_height in adj_heights:
                if height > block_height:
                    lst.append(height - block_height)
                else:
                    pass
            
            block_area = sum(lst) + area_threshold

            total += block_area
    
    return(total)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
