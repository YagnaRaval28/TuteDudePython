#Tuple
#(Item1, Item2, .....)
# sequence of item as a collection
# immutable
"""tuple1=("Python",1,True,None,[1,26,25],8.9)
print(len(tuple1))
print(tuple1[0])
print(tuple1[-1])
list=[1,2,3]
print(list,type(list))
#Typecast
t1=tuple(list)
print(t1,type(t1))"""

#There are multiple operations can be performed using tuple like
#Concatenation, repetition(* operator), membership (in,not in operator)
# count, index
# min, max, sum

#Concatenation
tuple1=(1,2,"John")
tuple2=(5,6,15)
print(tuple1+tuple2)


tuple=(1,2,4,56,798,85)
print(tuple.index(4))# what is the index of 4 in tuple
print(tuple.count(1)) # what is the count of 1 in tuple
print(min(tuple))
print(max(tuple))
print(sum(tuple))