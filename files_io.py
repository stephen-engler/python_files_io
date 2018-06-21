myfile = open('myfile.txt')
print(myfile.read())
#can aonly read once
myfile.seek(0)
mycontent = myfile.read()
print(mycontent)
#returns a list of lines
myfile.readlines()

#file locations
#need full file path
#pwd

#best practice to close it
myfile.close()

#or
with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()

print(contents)
#can read or write 
#a append r read w write r+ read and write w+ writing reading overwrite existing file
#with open('myfile.txt', mode='w') as myfile:

with open('mynewfile.txt', mode='r') as f:
    print (f.read())

with open('mynewfile.txt', mode='a') as f:
    f.write('four on fourth')

with open('mynewfile.txt', mode='r') as f:
    print (f.read())

with open('dadasf.txt', mode='w') as f:
    f.write('i created this file')
with open('dadasf.txt', mode='r') as f:
    print(f.read())
