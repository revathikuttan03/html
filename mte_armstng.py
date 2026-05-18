num=int(input("enter a number: "))
a=num
length=(len(str(num)))
i=0
result=0
while i <length:
    value=num%10
    num//=10
    i+=1
    result +=value**length 
if a==result:
    print("This is armstrong number")
else:
    print("This is not armstrong number")

import pandas as pd
data={'name' :[],'age':[],'email':[],'phone number':[]}
x=True
while x:
    choice=input("enter your choice:")
    match choice:
        case"add":
            a=input("Enter your name:")
            b=int(input("Enter your age:"))
            c=input("Enter your email id:")
            d=int(input("Enter your mobile number"))
            data