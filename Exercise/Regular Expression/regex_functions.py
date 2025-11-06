import re

s1 = "We are learning regex in python"
pat = r"[A-Z][a-z]"
mat = re.match(pat, s1)
print(mat)

phones = "XYZ-9865426894 , ABC- 3657894598"
pat = r"\b[0-9]{10}\b"
mat = re.findall(pat, phones)
print(mat)

phones = "XYZ-9865426894012255698 , ABC- 365789459889"
pat = r"\b[0-9]{7,15}\b"
mat = re.findall(pat, phones)
print(mat)

#finditer
phones = "XYZ-9865426894012255698 , ABC- 365789459889"
pat = r"\b[0-9]{7,15}\b"
mat = re.finditer(pat, phones)
for matches in mat:
    print(matches)

# sub()
s1="Sunday,Monday,Tuesday,Monday,Sunday,Saturday"
pat="S[a-z]+"
rep="Friday"
match=re.sub(pat,rep,s1)
print(match)

message= "We are learning re. using re we can search for pattern using a given string"
pat=r"\bre\b"
rep="Regular Expression"
match=re.sub(pat,rep,message)
print(match)

# compile()
phones="Alice-1547863245, Bob-8965472315, Mark-12368954789"
pattern=r"\d{10}"
compiled=re.compile(pattern)
match_obj=re.findall(compiled,phones)
print(match_obj)