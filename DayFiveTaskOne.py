'''
A random variable, X, follows Poisson distribution with mean of 2.5. Find the probability with which the random variable X is equal to 5.
'''
import math

# Variable declaration
mean_of_x = float(input())  #avg
k = float(input()) # k=5  
e=2.71828

# Poisson calculation
def calculate_poisson():
    result = ((mean_of_x**k)*(e**-(mean_of_x)))/math.factorial(k)
    print(round(result,3))

calculate_poisson()