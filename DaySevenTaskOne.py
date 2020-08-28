import math
"""
Given two n-element data sets, X and Y, calculate the value of the Pearson correlation coefficient.
"""
# Variables
size = int(input())
dataset_x = [float(n) for n in input().split()]
dataset_y = [float(m) for m in input().split()]

# Standard deviation calculation
def calculate_stdev(nums):
    sums = 0.0
    sums_coll = sum(float(n) for n in nums)
    mean_nums = sums_coll/size
    for i in range(size):
        sums += (float(nums[i]) - float(mean_nums))**2
    return math.sqrt((1/size)*sums)

# Covariance calcualation
def calculate_covariance(): 
    sum_cov = 0  
    mean_x = float(sum(dataset_x)/len(dataset_x))
    mean_y = float(sum(dataset_y)/len(dataset_y))
    for i in range(size):
        sum_cov += float((dataset_x[i] - mean_x)*(dataset_y[i] - mean_y))
    return float((1/size)*(sum_cov))

# Pearson coefficient calculation
def calculate_pearson_coef():
    return calculate_covariance()/(calculate_stdev(dataset_x)*calculate_stdev(dataset_y))

#Print result with 3 decimals
print(round(calculate_pearson_coef(),3))