from re import A


a = int(input("Enter the 1st number :"))
b = int(input("Enter the 2nd number :"))
print("The before swap numbers is ",a, "and" ,b)
temp = a
a = b
b = temp 
print("The after swap numbers is ",a, "and" ,b)
