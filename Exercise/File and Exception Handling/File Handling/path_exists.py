"""
import os
file_name="example.txt"
if os.path.exists(file_name):
    print("File Exists")
else:
    print("File doesn't exists")  
"""

from pathlib import Path
file_name=Path("example1.txt")
if file_name.exists():
    print("File Exists")
else:
    print("File doesn't exists, creating a new file")
    fh=open(file_name,'xt')
    fh.write("Some content")
    fh.close() 
  