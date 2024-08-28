# strings
#1.reverse a string.
'''x=input("string :")
s=""
for i in range(len(x)-1,-1,-1):
    s+=x[i]
print(s)'''

#2.count the number of vowels in a string
'''x=input("string:")
x=x.lower()
count=0
for i in range(len(x)):
    if x[i]=="a" or x[i]=="e" or x[i]=="i" or x[i]=="o" or x[i]=="u":
        count+=1

print(f'vowels in {x} is {count}')'''

#3 to remove all duplicates from a string
'''x=input("string :")
y=""
for i in range(len(x)):
    if x[i] not in y:
        y+=x[i]

print(y)'''

#4.check if two strings are anagrams.-->anagram:with all the letters in the words has to be equal
'''x=input("string :")
y=input("string2 :")
flag=False
if len(x)==len(y):
    for i in range(len(x)):
       if x[i] in y:
           flag=True
       else:
           flag=False
           break


    if flag==True:
        print("both are anangrams")
    else:
        print("not anagrams")

else:
    print("not anagrams")'''
'''
logic: 1.check the length of the strings
       2.sorting the strings then we can get to know all the  caracters will be sorted there we will check how many times it has each alphabet will be adjacent
       3.as strings are not the mutable we have to convert them into list and  then join into the string
'''
'''def anagram(s,r):
    s=s.replace(" ","").lower()
    r=r.replace(" ","").lower()
    s=list(s)
    r=list(r)
    if len(s)==len(r):
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if ord(s[i])>ord(s[j]):
                    temp=s[i]
                    s[i]=s[j]
                    s[j]=temp


        for i in range(len(r)):
            for j in range(i+1,len(r)):
                if ord(r[i])>ord(r[j]):
                    temp = r[i]
                    r[i] = r[j]
                    r[j] = temp

    if ''.join(s)==''.join(r): #list to string
        print("both are anagrams")
    else:
        print("not anagrams")


s=input("string 1:")
r=input("string 2:")
anagram(s,r)'''


# 5.a function to find the longest common prefix among a list of strings
'''
def common_prefix(lt):
    lt=sorted(lt)
    if not lt:
        return ""
    else:
        prefix=lt[0]
        for i in lt[1:]:
            while not i.startswith(prefix):
                prefix=prefix[:-1]

                if not prefix:
                    return ""
        return prefix

lt=list(map(str,input().split()))
y=common_prefix(lt)
print(y
