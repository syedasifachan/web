def primerange(s,e):
    for i in range(s,e+1):
        if(prime(i)==True):
            print(i,end='')
s,e=int(input()),int(input())
primerange(s,e)
