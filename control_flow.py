# If statement
n=11
if n % 2==0:
    print("The number is even")
print("The number is odd")


# If else Statemant
n=5
if n % 2 == 0:
    print("\n n is a even number")
else:
    print("n is odd")



# Elif (Nested) Statements:  Nested if statements are if statements inside another statements

a = 55; b = 10; c=155
if a>b:                                  # using and operator v can 
    if a>c:
        print("a value is bigger")
    else:                                #Depends on the values else is needed
        print("c value is biger")
elif b>c:
    print("b value is bigger")
else:
    print("c is Bigger")



# If-elif-Eles:  Above example

# For loops

lst = [1,5,6,7]
for i in range(len(lst)):
    print(lst[i],end ="")
print("\n")
for j in range (0,10):
    print ( j, end = "")
print("\n")

#repeat code for while loops 
m=5
i=0
while i < m:    
    print(i,end = " ")
    i =i + 1  
print("\n End")    

# For break

for i in range(10):
    print(i,end=" ")

    if i == 5:
        print("\n Break applied")
        break
print(" Outside loop")    
print("\n")

# Continue

for var in "Python world":
    if var== "w":
        continue
    print(var)