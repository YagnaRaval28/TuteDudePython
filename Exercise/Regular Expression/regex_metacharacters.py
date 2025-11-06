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

match_object=re.search("[0-9].[0-9][0-9]",message)
print(match_object)

match_object=re.search("[0-9].[0-9]","House no-251/A")
print(match_object)

# . matches any character except new line character (\n)