#1.find the factorial of a number.--.using loop
'''def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i

    return fact

n=int(input("enter number:"))
print(f'factorial of {n} is {factorial(n)}')'''

#2.check if a number is prime or not
'''def check_prime(n):
    c=0
    if n==1:
        print("1 is neither prime nor composite")
    else:
        for i in range(1,n):
            if n%i==0:
                c+=1

        if c>=2:
            print("not prime,it is composite number")
        else:
            print("prime")


n=int(input("num>"))
#print(check_prime(n)) #it retuen s the none as the print in the print function
check_prime(n)'''

#3.prime numbers in a range
'''def prime_range(n):
    lt=[]
    for i in range(2,n+1):
        c=0
        for j in range(2,i):
            if i%j==0:
                c+=1

        if c ==0:
            lt.append(i)

    return lt

n=int(input("num>"))
print(prime_range(n))'''

#sum of digits in the number
'''def sum_digits(n):
    total=0
    n=abs(n)  # Handle negative numbers
    while n>0:
        i=n%10
        total+=i
        n=n//10

    return total

n=int(input("number>"))
print(sum_digits(n))'''


#factors of the number
'''def factors(x):
    fact=[]
    for i in range(1,x+1):
        if x%i==0:
            fact.append(i)

    return fact

n=int(input("num>"))
print(factors(n))'''


#gcd or the hcf bothe mean the same when it comes to the mathematics and they refer to the highest number which can didivide the both numbers without leaving the remainder
# gcd for the euclidean algorithm
'''def gcd(a,b):
    while b != 0:
        a,b=b,a%b
    return a



def lcm(a,b):
    if a==0 or b==0:
        return 0
    else:
        g=gcd(a,b)
        l=abs(a*b)//g
        return l

a=int(input(">"))
b=int(input(">"))
print(f"gcd :{gcd(a,b)}")
print(f"lcm :{lcm(a,b)}")'''
