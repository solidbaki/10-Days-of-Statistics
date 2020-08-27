"""
The number of tickets purchased by each student for the University X vs. University Y football game follows a distribution that has a mean of 2.4 and a standard deviation of 2.0.

A few hours before the game starts, 100 eager students line up to purchase last-minute tickets. If there are only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?
"""
import math

tickets_left = float(input())
num_of_stds = int(input())
mean_of_game = float(input())
stds_stdev = float(input())

stdev = stds_stdev * math.sqrt(num_of_stds)

cdf = 0.5 * (1 + math.erf((tickets_left - mean_of_game * num_of_stds) / (stdev * math.sqrt(2))))

print(round(cdf,4))
