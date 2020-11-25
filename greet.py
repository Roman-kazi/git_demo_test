import random

def greet(name):
    print("Hello,", name)

greet(input("Enter name: "))

def play():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print("What is ",a," + ",b)
    ans = int(input())
    if a+b == ans:
        print("Nice")
    else:
        print("Go to elementry school")
play()
