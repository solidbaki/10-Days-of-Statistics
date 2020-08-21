# Enter your code here. Read input from STDIN. Print output to STDOUT
#Calculate mean,median and mode
#First input is for array size N, second input is for array elements
N = int(input())
set_of_integers = [int(n) for n in input().split()]
total = 0

for i in range(N):
    total += int(set_of_integers[i])

#Calculate mean, print it with one decimal
mean = total/N
print(round(mean,1))

#Calculate median, print it with one decimal
set_of_integers.sort()
median = (set_of_integers[int(N/2)] + set_of_integers[int((N/2)-1)]) / 2
print(round(median,1))

#Calculate mode, print it 
list_of_occurences = []
max_num_of_occurence = 0

#Calculating maximum number of occurences
for num in set_of_integers:
    list_of_occurences.append(set_of_integers.count(num))
    if set_of_integers.count(num) >= max_num_of_occurence:
        max_num_of_occurence = set_of_integers.count(num)
#Print the first value with the number of occurence
#Considering the list is already sorted, first value encountered with
#maximum num of occurence will be the minimum one, which is the one we are looking for
for i in range(N):
    if set_of_integers.count(set_of_integers[i]) == max_num_of_occurence:
        print(set_of_integers[i])
        break