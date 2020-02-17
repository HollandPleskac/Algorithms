#10 linear search
A = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def linear_search(A,data_to_find):
    for x in range(len(A)):
        if data_to_find == A[x]:
            return x
    else:
        return -1
print(linear_search(A,input("enter the letter(a-z) that you would like to find : ")))
print()
#iterative binary search
print('Iterative Binary Search - finding letter j')
print()
letterToFind = 'j'
l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
min_index = 0
max_index = len(l) - 1
print("min index: ",min_index)
print("max index: ",max_index)
print("guess index: ",(min_index + max_index)//2)
while True:
    guess_index = (min_index + max_index) //2
    print("min index",min_index)
    print("max index",max_index)
    print("guess index",guess_index)
    if l[guess_index] == letterToFind:
        print(letterToFind," found at index",guess_index)
        break
    elif l[guess_index] < letterToFind:
        min_index = guess_index +1
    elif l[guess_index] > letterToFind:
        max_index = guess_index-1
    elif min_index>=max_index:
        print(l[len(l)-1]," found at index",len(1)-1)
