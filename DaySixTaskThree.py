"""
You have a sample of 100 values from a population with mean 500 and with standard deviation 80. Compute the interval that covers the middle 95% 
of the distribution of the sample mean; in other words, compute A and B such that P(A<x<B)=95. Use the value of z 1.96 Note 
that z is the z-score.
"""
# Variables
num_of_population = float(input())
mean = float(input())
sd = float(input())
interval = float(input())
z = float (input())

#Standard deviation of sample
sd_sample = sd / (num_of_population**0.5)

print(round(mean - sd_sample*z,2))
print(round(mean + sd_sample*z,2))