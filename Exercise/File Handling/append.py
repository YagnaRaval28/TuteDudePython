"""
# if file doesn't exists 'a' mode creates file
fh = open("example.txt", "at")

fh.write("\nThis content has been written through 'a' mode\n")
fh.write("'a' mode is used to add new content at the end of the file\n")
fh.write("Good bye!\n")

fh.close()
"""

fh=open("example.txt",'r')
contents=fh.read()

print(contents)
