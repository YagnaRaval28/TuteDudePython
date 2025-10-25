#Fronzen sets are immutable
fs1=frozenset({1,2,3})
print(fs1,type(fs1))

# We can't change the frozen set

# can perfrom union,intersection and different elements
fs2=frozenset({2,3,4})
print(fs1&fs2)
print(fs1|fs2)
print(fs1-fs2)
