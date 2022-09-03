from itertools import count


list1=[1,2,3,4,5]
list2=["A","B","C","D","E"]
list3=["hello","hey","hi"]
#print(cmp(list1,list2))
print(min(list1))
print(max(list1))
print(tuple(list3))
print(set(list3))
zipped = zip(list1,list2)
print(zipped)
print(dict(zipped))
list1.append(list2)
print(list1)

print(len(list1))
print((list1))