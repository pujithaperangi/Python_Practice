#prime number implementation using exception handling

def prime_check(n):
    try:
        c=0
        for i in range(2,n):
            if n%i==0:
                c+=1

        '''if c==0:
            print("prime")
        else:
            print("not prime")'''

    except ValueError:
        print("invalid / not suitable literals")
    except NameError:
        print("variable doesn't exist")
    except Exception as ex:
        print(ex)
    else:
        if c == 0:
            print("prime")
        else:
            print("not prime")

    finally:
        print("execution completed")


n=int(input("->"))
if n<=1:
    print("invalid input")
else:
    prime_check(n)
