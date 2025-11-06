import re
message="Python current version is 3.13 . Previous versions are 3.12,3.11,3.10 ."

match_object=re.search("[0-9][0-9]",message)
print(match_object)
'''
match_object=re.search("[0-9][0-9]","House no-251/A")
print(match_object)

match_object=re.search("[0-9][0-9][0-9]","House no-251/A")
print(match_object)
'''

match_object=re.findall("[0-9].[0-9][0-9]",message)
print(match_object)

match_object=re.search("[0-9].[0-9]","House no-251/A")
print(match_object)

# . matches any character except new line character (\n)

# ^
s1="Python is a programming language"
pat=r"[a-z]{7}"
match_object=re.search(pat,s1)
print(match_object)


# $ - ends with the string

# groups() -
emails="abc_123@example.com"
pat=r"(com|edu)"
match_object=re.search(pat,emails)
print(match_object)