# Open a file
# open(file_name,mode_to_open)
# modes- w-write,r-read,a-append,x-create
# text file and binary files t for text and b for binary

fh=open("example.txt","r")
print(fh)
fh.close()