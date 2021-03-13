print("------SIMPLE CALCULATOR-------")
# for user input

a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))

# Program for simple calculator functions

print("Press 1 for addition")
print("Press 2 for subtraction")
print("Press 3 for multiplication")
print("Press 4 for division")

c = int(input("Enter your choice\n"))

if c == 1:
    print("Sum is : ",a+b)
elif c == 2:
    print("Substraction is : ",a-b)
elif c == 3:
    print("Multiply is : ",a*b)
elif c == 4:
    print("Division is : ",a/b)
else:
    print("Invalid input")



