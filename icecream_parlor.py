import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    # Write your code here
    d = dict(zip(arr,range(len(arr))))
    for i in range(len(arr)):
        j = d.get(m - arr[i])
        if j != None:
            return [i+1,j+1]

if __name__ == '__main__':
    fptr = open('C://Users/iamwl/Documents/projects/myOutput.txt', 'w')

    with open('C://Users/iamwl/Documents/projects/input02.txt') as f:
        lines = f.readlines()

    t = int(lines[0].strip())

    for t_itr in range(t):
        m = int(lines[3*t_itr+1].strip())

        n = int(lines[3*t_itr+2].strip())

        arr = list(map(int, lines[3*t_itr+3].rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
