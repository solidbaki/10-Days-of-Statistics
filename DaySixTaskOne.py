"""
A large elevator can transport a maximum of 9800 pounds. Suppose a load of cargo containing 49 boxes must be transported via the elevator. The box weight of this type of cargo follows a distribution with a mean of 205 pounds and a standard deviation of 15 pounds. Based on this information, what is the probability that all 49 boxes can be safely loaded into the freight elevator and transported?
"""
import math

max_weight = int(input())
num_of_boxes = int(input())
mean_of_boxes = int(input())
std_dev = int(input())

mu_sum = num_of_boxes * mean_of_boxes 
sigma_sum = math.sqrt(num_of_boxes) * std_dev

def calculate_cdf(max_weight, mean_of_boxes, std_dev):
    Z = (max_weight - mean_of_boxes)/std_dev
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

print(round(calculate_cdf(max_weight, mu_sum, sigma_sum), 4))