# List declaration of same type

places = ['Jaipur','Delhi','Gurgaon','Panaji']
print(places)
places.append('Bhagalpur')
print(places)

# list declaration of different types

people = [1, 'Jai', 2, 'Bubna']
print (people)

print(places == people)  # compare one list with other

# append in list
nums = [1,5,9,3]
nums.append(7)
print(nums[0:])

# get the data by indexing in list
List =[1,2,23,35,49,55]
print(List[:3])    # It will print till 3rd number
print(List[-3:])   # It will print from back side

# Iterating a List

names = ["John","Sangam","Danish","Helen","Doremon"]
for i in names:   # The i variable will iterate over the elements of the lISTS
    print (i)

#=============================
#Declaring the empty list

li =[]
n = int(input("Enter the number of elements: \n"))  #Number of elements are entered by the user
for i in range(0,n):
    li.append(input("Enter the data\n"))
print("The datas are:\n")
for i in li:
    print(i,end =", ")
