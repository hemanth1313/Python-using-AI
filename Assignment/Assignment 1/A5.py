p = int(input("Enter the priciple amount :"))
t = int(input("Enter the time in years  :"))
r = int(input("Enter the rate of intrest :"))
n = int(input("Entre the n value :"))
CI=p*(1+(r/n)**n*t)-p
print("Compound Intrest =",round(CI,3))