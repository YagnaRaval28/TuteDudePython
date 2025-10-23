"""#Slicing of lists
list=[1,2,3,4,5,6,7,8]
print(list[1:6:2])

#Concatenation of lists
l1=[1,5,7]
l2=[2,6]
print(l1+l2)

#Repetation of lists
print(l2*2)

#Adds item at the end- append()
l2.append(7)
print(l2)

#Adds item before specific index- insert(index,item)
l2.insert(1,5)
print(l2)

#Can add multiple item-extend()
l2=[2,5]
l2.extend([5,6,7])
print(l2)

#to remove an element- remove()
l2.remove(5)
print(l2)

#pop()- will delete last element if not given any index
l2.pop(1)
print(l2)

#Reverse a list
days_of_week=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
days_of_week.reverse()
print(days_of_week)

#Sort the list
nums=[9,2,7,6,1,0]
nums.sort()
print(nums)"""

nums=[0,5,6,9,0,1,2,5,7,9,2,2]
num=int(input("Enter number which you want occurance of:"))
c=nums.count(num)
print(f"Occurance of {num} is {c}")


#in and not in is a membership operation weather item is present in the list or not