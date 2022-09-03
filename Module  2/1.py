#Program to show various ways to read and write in a file

file1 = open("myfile.txt","w")
L= ["This is Delhi \n","This is Paris \n","This is London"]

# \n is placed to indicate EOL (End of the line)
file1.write("HEllo \n")
file1.writelines(L)

file1.close()  #to change file access modes
file1 = open("myfile.txt","r+")
print("Output of the read function is")
print(file1.read())
print()

# seek (n) takes the file handel to the nth
# bite from the beginning
file1.seek(4)

print(" Output of Readline functio  is")
print(file1.readline())
print()

file1.seek(0)
# to shiw diiference between read and readline
print("Out of read (100) function is ")
print(file1.read(100))
print()
file1.seek(0)
print("output of the Readline(100) function is")
print(file1.readline(100))
file1.seek(0)

# readlines function 
print("Output of the readlines fnction")
print(file1.readlines())
print()
file1.close()