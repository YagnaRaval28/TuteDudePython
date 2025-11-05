try:
    with open('Sample.txt','rt') as fh:
        data=fh.readline()
        print(f"Line 1:{data}")
        data1=fh.readline()
        print(f"Line 2:{data1}")
except FileNotFoundError as e:
    print("Sample.txt does not exists")
    print(e)                