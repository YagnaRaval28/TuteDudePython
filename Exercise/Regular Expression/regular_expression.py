str="Python current version is 3.13 . Previous versions are 3.12,3.11,3.10 ."
"""
#if python present in string or not
print("Python" in str)

print(str.find("Python"))
print(str.find("3.13"))
import re


re.search(pattern,string)
=> returns a match  object when there is a match found else None
"""
import re

print(re.search('3.',str))
print(str[26:28])