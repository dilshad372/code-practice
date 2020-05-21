# https://www.hackerrank.com/challenges/flatland-space-stations/problem


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    lst = list()
    
    for i in range(n):
        lst.append(0)
    
    for j in c:
        lst[j] = 1
    
    dist = list()
    count = 0

    for i in lst:
        if i == 1:
            if dist:
                dist.append((count+1)//2)
            else:
                dist.append(count)
            count = 0
        else:
            count += 1
    
    dist.append(count)
    
    return max(dist)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
