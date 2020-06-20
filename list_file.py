import os
#get the list of path
# files_path = os.listdir("C:\\Users\\RAMESH\\Downloads")
files_path = os.walk("C:\\Users\\RAMESH\\Downloads")
#all list of directory and subdirectory
for item in files_path:
    print(item)