#Nested for 

Tuple1 = (0,1,2,3)
Tuple2 = ('Python','Programming','World','of')
Tuple3 = (Tuple1 , Tuple2)
print(Tuple3)

Tuple4 = Tuple1 + Tuple2
print(Tuple4)

Tuple5 = Tuple4 + Tuple3
print(Tuple5)

print(Tuple5[7][0])