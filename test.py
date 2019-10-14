import os
'''
Test on a non existing file
'''
# read and print the content of a non-existingfile  "file.txt"
print("file.txt does not exist but will be created so this is an empty file")
f = open("file.txt", "a")
f.close()

# open and read the file after the appending:
f = open("file.txt", "r")
print("Here is the read content:")
print(f.read())
f.close()

# open and write some content in this file
content = input(
    "Please write any content you want to store in this file. When you finish, press enter:")
f = open("file.txt", "w")
f.write(content)
f.close()

# reopen and read the new content
f = open("file.txt", "r")
print("Here is the new content of the file:")
print(f.read())
f.close()

print("\n###################################################################################\n")
'''
Test on an existing file
'''
# open and write some content in this file
print("\nNow file.txt exists and its content is not empty. Now let's overwrite its content")
content = input(
    "Write any content you want to store in this file. Please note the old content will be overwritten. When you finish, press enter:")
f = open("file.txt", "w")
f.write(content + "\n" + content)
f.close()

# reopen and read the new content
f = open("file.txt", "r")
print("\nHere is the new content of the file that you have just written and will be copied twice in this file. Therefore the content will be written twice:")
print(f.read())
f.close()

print("\n###################################################################################\n")
print("Now the file will be deleted")
if os.path.exists("file.txt"):
  os.remove("file.txt")
  print("file.txt has been deleted")
else:
  print("The file does not exist")

print("\n###################################################################################\n")
'''
Test on a folder
'''
print("Now an empty folder will be created and then deleted")
newPath = "/directoryName"
if not os.path.exists(newPath):
    os.makedirs(newPath)
    print("/directoryName folder has been created:")
else:
    print("/directoryName folder already exists")



if  os.path.exists(newPath):
    os.rmdir(newPath)
    print("/directoryName folder has been removed")
else:
    print("/directoryName folder does not exist")