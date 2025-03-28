print("Calculate area of: ")
print("a: Circle ")
print("b: Rectangle ")

# print("Enter 'a' or 'b': ")
option=input("Enter 'a' or 'b': ")
if(option=='a'):
    r=int(input("Enter radius: "))
    print("Area of circle is: ",3.14*r*r)
elif(option=='b'):
    l=int(input("Enter length:"))
    b=int(input("Enter breadth: "))
    print("Area of rectangle is: ",l*b)
else:
    print("Enter valid option!!")