#Standard deviation calculation

import math
N = int(input())
set_of_numbers = [int(n) for n in input().split()]
inside = 0

#Calculate Mean
def calculate_mean():
    sum = 0
    for i in range(len(set_of_numbers)):
        sum += set_of_numbers[i]
    return sum/len(set_of_numbers)

mean = calculate_mean()

# Sum up squares of the values minus mean
for i in range(len(set_of_numbers)):
    inside += (set_of_numbers[i] - mean) ** 2

#Print values with one decimal
print(round(math.sqrt(inside/N),1))