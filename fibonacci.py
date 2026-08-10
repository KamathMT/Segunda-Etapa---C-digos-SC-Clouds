###FIBONACCI

###Função recursiva
def fibonacci_rec(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci_rec(n-2) + fibonacci_rec(n-1)
n=int(input("n: "))
print(fibonacci_rec(n))

###Função interativa
def fibonacci_int(n):
    a,b=0,1
    for i in range(n):
        a,b=a+b,a
    return a
n=int(input("n: "))
print(fibonacci_int(n))