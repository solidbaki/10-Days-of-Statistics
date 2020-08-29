"""
A group of five students enrolls in Statistics immediately after taking a Math aptitude test. Each student's Math aptitude test score, x, and Statistics course grade, y, can be expressed as the following list of (x,y) points:

If a student scored an 80 on the Math aptitude test, what grade would we expect them to achieve in Statistics? Determine the equation of the best-fit line using the least squares method, then compute and print the value of y when x=80.

Input Format
"""

x, y = [], []
for _ in range(5):
    i = input().split()
    x.append(int(i[0]))
    y.append(int(i[1]))
n = len(x)
x_sum = sum(x)
x_sum_sqr = x_sum**2
x_sqr_sum = sum([x_i**2 for x_i in x])
y_sum = sum(y)
sum_prod_xy = 0
for x_i,y_i in zip(x,y):
    sum_prod_xy += (x_i*y_i)
b = (n*sum_prod_xy - x_sum*y_sum) / (n*x_sqr_sum - x_sum_sqr)
y_mean = y_sum/n
x_mean = x_sum/n
a = y_mean - b*x_mean

x_test = 80
y_test = a + b * x_test
print(round(y_test,3))   