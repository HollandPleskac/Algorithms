#factorials the regular way
##list = []
##factorial = 1
##number = int(input("enter a number"))
##for i in range(1,number+1,1):
##    list.append(i)
##print(list)
##
##for i in list:
##    print(i)
##    factorial = factorial*i
##print("The factorial of the number is : ",factorial)

#factorials the recursion way

def factorial(n):
    if n == 1:
        return 1
    print(n)
    return factorial(n-1) * n
n = int(input("Number? "))
print(factorial(n))
