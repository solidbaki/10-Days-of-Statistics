'''
The probability that a machine produces a defective product is 1/3. What is the probability that the  defect is found during the first 5 inspections?
'''
#Function calculates and prints geometric distribution
def calculate_geometric_distribution(n,p):
    return float((q**(n-1))*p)

# Variables
p = 1/3
q = 1 - p
n = 5

# Calculation
print(round(sum([calculate_geometric_distribution(i, p) for i in range(1,n+1)]),3))