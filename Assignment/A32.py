List = [1,2,3,4,5,6,7,8,9,44,55,899,6676,71235,18964,2181123]
print("The elements of the list are",List)
print("These are odd number in the list")
for num in List:
    if (num % 2 != 0):
        print(num,end=" ")
    