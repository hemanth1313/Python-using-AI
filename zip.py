#ZIP zip() method takes iterable or containers and returs a single iterator object, having mapped values from all the containers

name=["ABC", "Bca"," BBA", "MBA"]
roll_no = [1,3,2,4]
#using zip() to map values
mapped = zip(name,roll_no)
print(set(mapped))
#it prints random 

# Python program to illustrate 
# enumerate function
L1 =["eat", "Sleep","Repeat"]
S1 ="Python"

#Creating enumerate objects
obj1 = enumerate(L1)
obj2 = enumerate(S1)

print("Return type : ",type(obj1))
#enumerate : starts the index from the given value
print(list(enumerate(L1,7)))
# Changing start index to 4 from 0
print(list(enumerate(S1,4)))