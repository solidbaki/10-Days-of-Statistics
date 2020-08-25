# Binomial distribution calculation
# n = 6, from 3 to 6
'''
The ratio of boys to girls for babies born in Russia is 1.9 . If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?
'''
import math

def calculate_combination(x,y):
    return math.factorial(x) / (math.factorial(y)*math.factorial(x-y))

result = 0
p=1.09/2.09
q = float(1-p)
n = 6

#Calculate binomial distribution
for i in range(3,7):
    result += calculate_combination(n,i)*(p**i)*(q**(n-i))

#Print result with 3 decimals
print(round(result,3))