# Program to find factorial of a number

num = int (input("Enter a number \n"))
fact = 1
if num == fact:
    print("The factorial of 1 is ", num)
else:
    for i in range(1,num+1):
        fact = fact*i
print("The factorial of  ", num, " is ", fact)
