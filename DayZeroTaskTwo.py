#Weighted mean calculation
size_of_arr_and_weight = int(input())
note_list = [int(m) for m in input().split()]
weight_list = [int(n) for n in input().split()]
sum_notes = 0
sum_weights = 0

#Each note multiplied by their weights and added
for i in range(size_of_arr_and_weight):
    sum_notes += (note_list[i] * weight_list[i])
#Sum of weights
for i in range(size_of_arr_and_weight):
    sum_weights += weight_list[i]

#Print result with one decimal
print(round(sum_notes/sum_weights,1))