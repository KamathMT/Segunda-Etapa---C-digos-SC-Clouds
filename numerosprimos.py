###Números Primos

###Função Recursiva
def primos_rec(n,primos):
    if n not in (0,1):
        primos_rec(n-1,primos)
        primos.append(n)
        for i in range(2,n-1):
            if n%i==0:
                primos.remove(n)
                break
    return primos
n=int(input("n: "))
primos=list()
print(primos_rec(n,primos))

###Função Iterativa
def primos_int(n,primos):
    for num in range(2,n+1):
        primos.append(num)
        for div in range(2,num-1):
            if num%div==0:
                primos.remove(num)
                break
    return primos
n=int(input("n: "))
primos=list()
print(primos_int(n,primos))