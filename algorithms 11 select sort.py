#11 select sort
# algorithm repeatedly finds the min element from the list and puts
# it at the beginning of the list - swaps smallest element and element at
# beginning of the list

#swapper code
##temporary = a
##a = b
##b = a

import time

A = [16,7543,123,7547,23,74,2,5,1,547,5,2,457,103,5405,9,5,55,99999,23456,2654765,84,3,7,736,3456,53676,4567,345,245,435,435,245,5,4,83,236,54,73,567,568,5,42,6,45,756,7,67,3,6456,45,7,567,65,8,678,76,978,467,54,7,567,6,867,89,67,9,768,56,7,356,73576,3,76,657,68,678976,9,74,86,7,35657,65,7,876,9,5746245,2345,423,5,324,532,45,34,25,324,5,234,5,324,5,324,5,3245,324,53,245,324,5,324,5,324,5,234,5,4325,432,53,245,4,325,324,5,234,5,324,5,324,53,425,23,45,34,5,324,5,3245,34,25,43253245432,5,23,45,432,5,43,5,234,5324,5,342,5,342,5,324,5,3425,324,5,324,5,324,5,3245,324,5,432,5,432,5,324,53,45,43,25,324,5,324,5324,5,342,5,324,5,3425,23,45,324,5,324,53,245,324,5,324,5,3245,324,5,324,5,324,5324,5,234,5,324,5,34,5,2345,324,5,43,5,342,5432,57,63,7,54,376,58776,98,468,653,6,52,6,4326,57,56,8765,4,3,6,54,36,53,57,65,8,768976,48,653,76,43,65,43,6546,5,768,759,789,579,67,86,57,56,7,86,64,8,465,7,34,7653,7657,68,56,56,536,7,456,557,56,7,6466,77]

#print("list before ",A)
j=0

for j in range(len(A)):
    min_index = j

    #other index is the index that will be swapped with min_index

    value=A[min_index]
    for i in range(j,len(A)):
        if A[i] < value:
            min_index = i
            value =A[i]
    #print(min_index, A[min_index])


    temporary = A[min_index]
    A[min_index] = A[j]
    A[j] = temporary
print("list after ",A)

#function for getting the run time - after program run type time_it() into the shell

def time_it():
    start = time.clock()
    print('select sort')
    return (time.clock() - start)*1000
