#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)


mystr=""    
for j in range(m):
    for i in range(n):
        mystr+=matrix[i][j]
        

mystr=re.sub(r'\b[^a-zA-Z0-9]+\b',' ',mystr,re.DOTALL) #/b -> word boundary, ^ -> negate, [] -> capture group, + -> one or more occurrence, re.DOTALL -> find all matches (global mode)
print(mystr)