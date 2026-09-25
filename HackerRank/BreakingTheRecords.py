# Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. 
# She tabulates the number of times she breaks her season record for most points and least points in a game. 
# Points scored in the first game establish her record for the season, and she begins counting from there.
import math
import os
import random
import re
import sys

def breakingRecords(scores):
    lowScore = 0
    highScore = 0
    pAlto = scores[0] 
    pBajo = scores[0]
    for i in range(n):
        if pAlto < scores[i]:
            pAlto = scores[i]
            highScore += 1
        if pBajo > scores[i]:
            pBajo = scores[i]
            lowScore += 1
    return(highScore, lowScore)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()