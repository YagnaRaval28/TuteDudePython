student1={'Maths':90,'English':88,'Gujarati':82,'Hindi':82,'Science':87,'SS':86}
print(student1)
#Fetch the marks for Science
print(student1['Science'])

#get()
print(student1.get('Gujarati'))

#membership
print(90 in student1)
print('Maths' in student1)

student2={'Chemistry':62, 'Physics':64}
student1.update(student2)
print(student1)

student2={'Chemistry':80, 'Physics':64,'Biology':50}
student1.update(student2)
print(student1)

student1.pop('Biology')
print(student1)

#Keys cannot be duplicated in dict