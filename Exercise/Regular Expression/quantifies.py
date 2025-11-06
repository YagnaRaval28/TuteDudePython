import re 
str="Python current version is 3.13 . Previous versions are 3.12,3.11,3.10 ."

pat=r"[A-Z][a-z]{5}"
match_obj=re.search(pat,str)
print(match_obj)

# + => matches 1 or more repetations of the previous pattern
pat=r"[A-Z][a-z]+"
match_obj=re.search(pat,str)
print(match_obj)

# ? => 0 or 1 repetations of the previous pattern
pat=r"[A-Z][a-z]?"
match_obj=re.search(pat,str)
print(match_obj)

# * => 0 or more repetations of the previous pattern
pat=r"[A-Z][a-z]*"
match_obj=re.search(pat,str)
print(match_obj)

