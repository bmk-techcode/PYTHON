n=int(input("Enter the value of n:"))



def factorial(n):
    fact=1

    if n==1:
        print(fact)
        
    for i in range(1,n+1):
        fact=fact*i

    print("FACTORIAL IS",fact)
    
factorial(n)
