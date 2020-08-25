'''
The probability that a machine produces a defective product is 1/3. What is the probability that the  defect is found during the 5th inspection?
'''
# Variables
p = float(1/3)
q = 1 - p
n = 5

#Function calculates and prints geometric distribution
def calculate_geometric_distribution():
    result = (q**(n-1))*p
    print(round(float(result),3))

calculate_geometric_distribution()