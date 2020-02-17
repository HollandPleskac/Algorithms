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

##def factorial(n):
##    if n == 1:
##        return 1
##    print(n)
##    return factorial(n-1) * n
##n = int(input("Number? "))
##print(factorial(n))

#pascal's triangle the regular way
##print(1)
##layer = [1, 1]
##layers = 1
##while layers < 10:
##    for elem in layer:
##        print(elem,end=' ')
##    print()
##    new_layer = []
##    for i in range(len(layer)-1):
##        num1 = layer[i]
##        num2 = layer[i+1]
##        new_layer.append(num1 + num2)
##    new_layer=[1] + new_layer + [1]
##    layer=new_layer
##    layers+=1

#pascal's triangle the recusrive way

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
