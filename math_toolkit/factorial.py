# num=int(input("Enter the number: "))

def factorial(num):
    if num==1:
        return 1
    return num*fact(num-1)

#print(fact(num))