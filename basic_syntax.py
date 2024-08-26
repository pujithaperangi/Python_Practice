# syntax and basic questions

#1.check number is even or odd--implementation  in object oriented paradigm
'''class Evenodd():
    def evenodd(self,n):
        if n%2==0:
            return "Even"
        else:
            return "Odd"


if __name__=="__main__":
    obj=Evenodd()
    n=int(input("enter number :"))
    print(f'{n} is {obj.evenodd(n)}')'''

#2.find largest of three numbers
'''def largest(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z

print("find largest number among 3 numbers")
x=int(input("first :"))
y=int(input("second :"))
z=int(input("third :"))

print(f'largest among {x} ,{y} and {z} is {largest(x,y,z)}')'''


#3.find swap two variables without using a temporary variable
'''def swap(x,y):
    x=x+y
    y=x-y
    x=x-y
    print(f'after swaping value of x={x} and y={y}')

x=int(input("x :"))
y=int(input("y :"))
swap(x,y)'''

# 4.Write a Python program to check if a string is a palindrome.
'''def palindrome(n):
    n=str(n)
    for i in range(len(n)//2):
        if n[i]!=n[-(i+1)]:
            print("not palindrome")
            break
    else:
        print("palindrome")

n=int(input("num :"))
palindrome(n)'''

# 5.Write a Python program to generate the first n Fibonacci numbers.
'''def fibonacci(n):
    a,b=0,1
    count=0
    fib=[]
    while True:
        if count==n:
            return fib
            break
        else:
            fib.append(a)
            a,b=b,a+b
            count+=1

n=int(input("count :"))
print(fibonacci(n))'''

# 6. to generate fibonnaci series untill  n
'''def fibonacci(n):
    a,b=0,1
    fib=[]
    while True:
        if a>n:
            return fib
            break
        else:
            fib.append(a)
            a,b=b,a+b


n=int(input("upto :"))
print(fibonacci(n))'''


#7.reverse of string
'''x=input("string :")
#reverse=x[::-1]
#print(f'reverse string : {reverse}')
reverse=""
for i in range(len(x)-1,-1,-1):
    reverse+=x[i]
print(str(reverse))'''

#8.max number in the list -taking from the input from the user
'''x=list(map(int,input().split(" ")))
max=x[0]
for i in range(1,len(x)):
    if max<x[i]:
        max=x[i]

print("largest number :",max ," at ",x.index(max))'''

#9.factorial
'''def fact(n):
    prod=1
    for i in range(1,n+1):
        prod*=i

    return prod

n=int(input("number:"))
print(f'{n}!={ fact(n)}')'''