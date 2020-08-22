N = int(input())
set_of_nums = [int(n) for n in input().split()]
set_of_nums.sort()
lower_half = []
upper_half = []

def calculate_median(set_of_numbers):
    if (len(set_of_numbers) % 2 == 0):
        return int((set_of_numbers[int(len(set_of_numbers)/2)] + set_of_numbers[(int(len(set_of_numbers)/2)-1)]) / 2)
    elif (len(set_of_numbers) % 2 == 1):
        return int(set_of_numbers[int((len(set_of_numbers)-1)/2)])

def calculate_lu_halves():
    #Lower and upper half sizes
    if (N % 2 == 0):
        lu_half_sizes = int((N / 2))
    elif (N % 2 == 1):
        lu_half_sizes = int((N - 1) / 2 )

    for i in range(lu_half_sizes):
        upper_half.append(set_of_nums[i])
        lower_half.append(set_of_nums[N-1-i])

calculate_lu_halves()
lower_half.sort()
upper_half.sort()

#Q1 = calculate_median(upper_half)
print(round(calculate_median(upper_half)))

#Q2 = calculate_median(set_of_nums)
print(calculate_median(set_of_nums))

#Q3 = calculate_median(lower_half)
print(round(calculate_median(lower_half)))