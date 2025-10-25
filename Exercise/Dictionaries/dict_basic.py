# comma separated key value pairs enclosed within {}
groceries={'milk':34,'bread':50,'butter':56}
print(groceries,type(groceries))
#It is access through key 
print(groceries['bread'])

#Dict are mutable
groceries['milk']=68 #updates the value of dict
print(groceries)

groceries['Peanut butter']=460 #adds new key value pair to dict
print(groceries)