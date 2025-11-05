# Compile time error => Syntax error & Indenation error
# Eceptions => errors using execution

#Handle exception using try and catch block
'''
num1=int(input("Enter a number:"))
num2=int(input("Enter another number:"))
try:
    result=num1/num2
    print("Result=",result)
except ZeroDivisionError:
    print("Denominator cannot be zero")
except ValueError:
    print("Numbers can be digits only")        

'''
import io
try:
    fh=open("example.txt",'rt')
    content=fh.read()
    fh.close()
except FileNotFoundError as e:
    print("The file you are trying to read does not exists")    
    print(e)
except io.UnsupportedOperation as e:
    print("Not readable file")
    print(e) 
# else and finally block are optional       
else:
    print("Else block")
    print(content) 
finally:
    print("Finallly Block")       