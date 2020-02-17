#bubble sort
#Task 1 Swapper Function : function that takes in a list of numbers and swaps the two numbers with index a and index b

##l = [1,2,3,4,5,6]
##print('l',l)
##def swapper(numbers,a,b):
##    c = numbers[a]
##    numbers[a] = numbers[b]
##    numbers[b] = c
##    print('numbers list: ',numbers)
##swapper(l,0,2)

#Task 2 Issorted Function : function that checks if the list is sorted least to greatest

##l = [1,2,3,4,5,6]
##def issorted(numbers):
##    for i in range(len(numbers)):
##        if i != len(numbers)-1:
##            if numbers[i] < numbers[i+1]:
##                pass
##            else:
##                return False
##    return True
##print(issorted(l))

#Task 3 Looping Over Consecutive Numbers function : function that loops over each pair of consecutive numbers

##l = [12, 1, 68, 3, 102, 99, 6]
##for i in range(len(l)-1):
##    num1 = l[i]
##    num2 = l[i + 1]
##    print(num1,' ',num2)
    #print("Num1: {} | Num2: {}".format(num1,num2))
    
#Task 4 Putting It All Together : putting the previous functions together to make a bubble sort
# - directions for this step at the bottom of the file

l = [1,12,18,4,7,5,6,12]
print('l',l)
def swapper(numbers,a,b):
    c = numbers[a]
    numbers[a] = numbers[b]
    numbers[b] = c
    print('list sorting... ',numbers)

l = [1,2,3,4,5,6]
def issorted(numbers):
    for i in range(len(numbers)):
        if i != len(numbers)-1:
            if numbers[i] < numbers[i+1]:
                pass
            else:
                return False
    return True


while not issorted(l):
    for i in range(len(l)-1):
        if l[i+1] < l[i]:
            swapper(l,i+1,i)
        num1 = l[i]
        num2 = l[i + 1]
        #print(num1,' ',num2)
print("Sorted List : ",l)




''' Directions for the Putting It All Together step:
 * Put your two functions, swapper and issorted, into a Python file.
 * Define an unsorted list, l, at the top of the code.
 * Create a while-loop like this: while not issorted(l):
 * This while-loop continues to loop as long as the list is not sorted.
 * Place your for-loop from Slide Four inside the while-loop.
 * In each iteration of the for-loop, check whether the second number of the pair is less than the first number. If it is, then swap the numbers using swapper.
 * When the while-loop ends, print out the sorted list.
'''
