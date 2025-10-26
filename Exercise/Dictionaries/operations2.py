# not allowed keys- list, set, dict => mutable datatyple
# allowed keys- str,int,float,bool,tuple => immutable datatypes

# keys only can be immutable datatype
# values can be any datatype
student1={'id':1000,'name':"Yagna",'marks':{'eng':90,'math':95,'sci':100}}
print(student1['marks']['math'])

#keys()- to fetch only keys
print(student1.keys(),type(student1.keys()))
# values()- to fetch only values
print(student1.values(),type(student1.values()))
# items()
print(student1.items(),type(student1.items()))