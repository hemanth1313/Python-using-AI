# sum of array
array = []
num = int(input("Entre the size of the array: "))
print("Entre the array elements")
for n in range(num):
    numbers = int(input())
    array.append(numbers)
print("Sum of array elements =",sum(array))
