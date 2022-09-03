from typing import List


List1 = ["Hello1",'Python1',["Hi","Python2"]]
List1[0] = "Hi"
List2 = ["Hello",'World',10,5.0,List1]
print(List2)

a = List1[0] + List2[1]
print(a)

List3 = List1 + List2
print(List3)
print(List3[1] + List3[4])

List4 = List3 + List2
print(List4)
print(List4[7][2])

List5 = List4 + List1
print(List5)
print(List5[7][2][1])