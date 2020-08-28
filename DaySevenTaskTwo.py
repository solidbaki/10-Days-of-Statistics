"""
Given two -element data sets, X and Y, calculate the value of Spearman's rank correlation coefficient.
"""

import math

# Variables
n = int(input())
dataset_x = [float(n) for n in input().split()]
dataset_y = [float(m) for m in input().split()]

# Sorted
rx = [sorted(dataset_x).index(i) for i in dataset_x]
ry = [sorted(dataset_y).index(i) for i in dataset_y]

# Spearmen rank correlation coefficient
rxy =1-(sum([(rx[i]-ry[i])**2 for i in range(n)])*6/(n*(n**2-1)))
print(round(rxy,3))