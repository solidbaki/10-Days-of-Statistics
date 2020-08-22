# Interquartile range calculation with frequencies
N = int(input())
elements = [int(n) for n in input().split()]
frequencies = [int(m) for m in input().split()]
elements_with_frequencies = []
lower_half = []
upper_half = []

#Create concatenated list
for i in range(N):
    for j in range(frequencies[i]):
        elements_with_frequencies.append(elements[i])

elements_with_frequencies.sort()

def calculate_median(elements_with_frequencies):
    if (len(elements_with_frequencies) % 2 == 0):
        return (elements_with_frequencies[int(len(elements_with_frequencies)/2)] + elements_with_frequencies[(int(len(elements_with_frequencies)/2)-1)]) / 2
    elif (len(elements_with_frequencies) % 2 == 1):
        return elements_with_frequencies[int((len(elements_with_frequencies)-1)/2)]

def calculate_lu_halves():
    N = len(elements_with_frequencies)
    #Lower and upper half sizes
    if (N % 2 == 0):
        lu_half_sizes = int((N / 2))
    elif (N % 2 == 1):
        lu_half_sizes = int((N - 1) / 2 )

    for i in range(lu_half_sizes):
        lower_half.append(elements_with_frequencies[i])
        upper_half.append(elements_with_frequencies[N-1-i])

calculate_lu_halves()
lower_half.sort()
upper_half.sort()

#Q3 - Q1 is interquartile range
print(float(round(calculate_median(upper_half)-calculate_median(lower_half),1)))