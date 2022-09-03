a = int(input("Enter the 1st number :"))
b = int(input("Enter the 2nd number :"))
c = int(input("Enter the 3rd number :"))
if a<b:
    if b<c:
        print("3rd  number is Largest")
if b<c:
    if c<a:
        print("1st number is Largest")       
else:
    print("2nd number is Largest")         
