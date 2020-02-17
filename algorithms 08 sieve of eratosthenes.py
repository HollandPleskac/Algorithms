#08 sieve of eratosthenes

##n = int(input("N? "))
##primes = list(range(2, n + 1))
##marked = [False] * len(primes)
##p = primes[0]
##while True:
##    if 2*p not in primes:
##        break
##    for i in range(primes.index(2 * p), primes.index(n) + 1,p):
##        marked[i] = True
##        
##    for i, x in enumerate(primes):
##        if x > p and not marked[i]:
##            p = x
##            break
##    if i == len(primes) - 1:
##        break
##for i, prime in enumerate(primes):
##    print(i)
##    print(prime)
##    if not marked[i]:
##        print(prime,end=' ')


#unfinished wikipedia version??????
##a = {2:True,3:True,4:True,5:True,6:True,7:True,8:True,9:True,10:True}
##for i in range(len(a.keys())):
##    if a[i] == True:
##        for 
