#recursion 02 w/ answers
# recursion is when a function calls itself
#ex.
##def function():
##    print('function called.')
##    function()

#fibonacci sequence of numbers without recursion
##import time
##a=1
##b=1
##c=None
##while True:
##    print(a)
##    c=a+b
##    a=b
##    b=c
##    time.sleep(1)
    
#fibonacci sequence the recursive way
##import time
##def fibonacci(a,b):
##    print(a)
##    time.sleep(1)
##    fibonacci(b,a+b)
##fibonacci(1,1)

#recursive factorial program
##def factorial(n):
##    if n == 1:
##        return 1
##    return factorial(n-1) * n
##n = int(input("Number? "))
##print(factorial(n))

#recursive pascals triangle
def pascal(layer):
    if len(layer)>10:
        return
    for e in layer:
        print(e, end=' ')
    print()
    new = []
    for n in range(len(layer)-1):
        new.append(layer[n]+layer[n+1])
    new = [1] + new + [1]
    pascal(new)
print(1)
pascal([1,1])
    
