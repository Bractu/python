#There will be two arrays of integers. Determine all integers that satisfy the following two conditions:
# 1.	The elements of the first array are all factors of the integer being considered
# 2.	The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. Determine how many such numbers exist.
import math
import os
import random
import re
import sys


def getTotalX(a, b):
    mayorA = max(arr)
    menorB = min(brr)
    count = 0
    for i in range(mayorA, menorB +1):
        condicionA = True
        for j in arr:
            if i % j != 0:
                condicionA = False
                break
        condicionB = True
        for b in brr:
            if b % i != 0:
                condicionB = False
                break
        if condicionA and condicionB:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
