"""
The manager of a industrial plant is planning to buy a machine of either type A or type B. For each day’s operation:

The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88. The daily cost of operating A is CA=160+40x^2.
The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55. The daily cost of operating B is CB=128+40y^2.
Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure that they operate like new at the start of each day. Find and print the expected daily cost for each machine.
"""

# Get input
inputs = [float(n) for n in input().split()]
mean_of_A = inputs[0]
mean_of_B = inputs[1]


# Cost calculation
CostX = 160 + 40*(mean_of_A + mean_of_A**2)
CostY = 128 + 40*(mean_of_B + mean_of_B**2)

print(round(CostX, 3))
print(round(CostY, 3))