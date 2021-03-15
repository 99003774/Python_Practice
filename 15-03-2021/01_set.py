# set example

places = {"Goa", "Bangalore", "Mysore", "Pune", "Delhi", "Gurgaon"}
#print(places)
places.discard("Bangalore");    # Removing one place from places

for i in places:
    print(i)

# Using Update function

places.update(["Patna"])    
print(places)