#   ?
#   ??
#   ???
#   ????

print("-----Pattern 1-----")

def my_pattern(a):    # user defined function 

    for i in range(0,a):
        for j in range(0,i+1):
            print(" ? ",end=" ")
        print("\r")

my_pattern(5)
