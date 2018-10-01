
def find_prime_fact(x):
    z=x
    factors=[]
    pnos = []
    i=2
    while i<z:
        k=2
        while k < z:
            prime = True
            for j in range(2,int(i/2)):
                if i%j==0:
                    prime = False
                    break
            if prime:
                #print(i)
                pnos.append(i)

                if z%i==0:
                    print(i)
                    z=int(z/i)
                    factors.append(i)
            k+=1
        i+=1
    if z!=1:
        factors.append(z)
    print(factors)

    def multiplier(x,n):
        if n==len(x)-1:
            return x[n]
        else:
            return x[n]*multiplier(x,n+1)
        
    print(multiplier(factors,0))

    print("The highest prime factor is ",max(factors))

x = int(input("Enter a number:  "))

while x != 'q':
    find_prime_fact(x)
    x = int(input("Enter a number: "))
    
