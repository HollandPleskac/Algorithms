#04 binary search
##number_to_find = 101
##l = [6,20,21,24,30,32,80,85,90,101]
##min_index = 0
##max_index = len(l) - 1
##print("min index: ",min_index)
##print("max index: ",max_index)
##print("guess index: ",(min_index + max_index)//2)
##while True:
##    guess_index = (min_index + max_index) //2
##    print("min index",min_index)
##    print("max index",max_index)
##    print("guess index",guess_index)
##    if l[guess_index] == number_to_find:
##        print(number_to_find," found at index",guess_index)
##        break
##    elif l[guess_index] < number_to_find:
##        min_index = guess_index +1
##    elif l[guess_index] > number_to_find:
##        max_index = guess_index-1
##    elif min_index>=max_index:
##        print(l[len(l)-1]," found at index",len(1)-1)

#binary search recursion
import time
number_to_find = 101
l = [6,20,21,24,30,32,80,85,90,101]
def binary_search(min_index,max_index):
    guess_index = (min_index+max_index)//2
    if l[guess_index] == number_to_find:
        print(number_to_find," found at index",guess_index)
    elif l[guess_index] < number_to_find:
        binary_search(guess_index+1,max_index)
    elif l[guess_index] > number_to_find:
        binary_search(min_index,guess_index-1)
    elif min_index>=max_index:
        print(l[len(l)-1]," found at index",len(1)-1)
binary_search(0,len(l)-1)
def time_it():
    start = time.clock()
    print('binary sort')
    return (time.clock() - start)*1000
