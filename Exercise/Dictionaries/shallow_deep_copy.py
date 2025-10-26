import copy
"""
l1=[1,2.5,[1,2,5],'Python']
#shallow copy
l2=copy.copy(l1)
#print(l2)
#print(id(l1))
#print(id(l2))
l1[0]=100
l1[2][0]=5
print(f"l1 -> {l1}")
print(f"l2 -> {l2}")"""

#deep copy
l1=[1,2.5,[1,2,5],'Python']
l2=copy.deepcopy(l1)
l1[0]=100
l1[2][0]=5
print(f"l1 -> {l1}")
print(f"l2 -> {l2}")