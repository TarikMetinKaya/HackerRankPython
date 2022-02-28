#Compiler Pyhton 3

#Say "Hello, World!" With Python
def q1():
    print("Hello, World!")


#Python If-Else
def q2():
    #!/bin/python3

    import math
    import os
    import random
    import re
    import sys



    if __name__ == '__main__':
        n = int(input().strip())
        
        if n%2==1:
            print("Weird")
        elif n%2==0 and 2<=n<=5:
            print("Not Weird")
        elif n%2==0 and 6<=n<=20:
            print("Weird")
        elif n%2==0 and 20<n:
            print("Not Weird")


#Arithmetic Operators
def q3():
    if __name__ == '__main__':
        a = int(input())
        b = int(input())
        print(f"{a+b}\n{a-b}\n{a*b}")


#Python: Division
def q4():
    if __name__ == '__main__':
        a = int(input())
        b = int(input())
        print(f"{a//b}\n{a/b}")

#Loops
def q5():
    if __name__ == '__main__':
        n = int(input())
        for i in range(n):
            print(i*i)

#Write a function
def q6():
    def is_leap(year):
        leap = False
        
        # Write your logic here
        if year%4==0:
            leap=True
            if year%100==0:
                leap=False
                if year%400==0:
                    leap=True
        else:
            leap=False
        
        return leap

    year = int(input())

#Print Function
def q7():
    if __name__ == '__main__':
        n = int(input())
        printable=""
        for i in range(1,n+1):
            printable=printable+str(i)
        print(printable)