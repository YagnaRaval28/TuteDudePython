import re
s1="Python is a programming language. python3.13 is the current verison"

# [A-Z] [a-z]
pattern=r"[A-Z][a-z][a-z]"
match_obj=re.search(pattern,s1)
print(match_obj)

#\d \D
# \d matches 1 digit character. It is similar to [0-9]
pattern=r"[a-z][a-z][a-z]\d"
match_obj=re.search(pattern,s1)
print(match_obj)

# \D matches 1 non-digit character. It is similar to [0-9]
pattern=r"[a-z][a-z][a-z]\D"
match_obj=re.search(pattern,s1)
print(match_obj)

# \s \S
# \s matches any white space character, tab and new line characater
pattern=r"[a-z][a-z][a-z]\s"
match_obj=re.search(pattern,s1)
print(match_obj)

s2="""Hi There
We are lerning python
"""
# \S is exactly opposite to \s. it matches except space,\n and \t
pattern=r"[a-z][a-z][a-z]\S"
match_obj=re.search(pattern,s2)
print(match_obj)

# \w matches [a-z] [A-Z] [0-9]
pattern=r"[a-z][a-z][a-z]\w"
match_obj=re.search(pattern,s1)
print(match_obj)

# \W matches  except [a-z] [A-Z] [0-9]
pattern=r"[a-z][a-z][a-z]\W"
match_obj=re.search(pattern,s1)
print(match_obj)