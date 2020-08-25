'''
A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:

No more than 2 rejects? - First line output
At least 2 rejects? - Second line output
'''

import math

#Function calculates combination
def calculate_combination(x,y):
    return math.factorial(x) / (math.factorial(y)*math.factorial(x-y))

result_less_than_two, result_more_than_two = 0,0
p= float(12/100)
q = float(1-p)
n = 10

# Binomial distribution for more than two rejects
for i in range(3):
    result_less_than_two += calculate_combination(n,i)*(p**i)*(q**(n-i))

# Binomial distribution for less than two rejects
for j in range(2,11):
    result_more_than_two += calculate_combination(n,j)*(p**j)*(q**(n-j))

# First line output
print(round(result_less_than_two,3))
# Second line output
print(round(result_more_than_two,3))