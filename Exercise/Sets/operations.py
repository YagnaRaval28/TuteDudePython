#Membership operator
nums={0,1,2,38,9,4}
print(0 in nums)
print(5 in nums)
print(10 not in nums)

#concatenation can't be done in sets
#Can't repeat sets

weekdays=('Mon','Tue','Wed','Thu','Fri','Sat','Sun') 
print(set(weekdays)) #in the output order of weekdays gets changing every time that proves that sets are non-sequntial

# sets are mutable
#add
nums.add(5)
print(nums)

#remove
nums.remove(5) #It gives error when element is not present in the set
print(nums)

#discard
nums.discard(0)
nums.discard(10) #It not give error when element is not present in the set
print(nums)