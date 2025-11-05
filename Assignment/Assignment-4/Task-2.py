data1=input("Enter text to write to the file:")
with open('output.txt','wt') as fh:
    fh.write(data1)
    fh.write("\n")
    print("Data sucessfully written to output.txt")

data2=input("Enter additional text to append:")
with open('output.txt','at') as fh:
    fh.write(data2)
    print("Data sucessfully append")

with open('output.txt','rt') as fh:
    print("Final content of output.txt\n")
    contents=fh.read()
    print(contents)        