
# Ope a file first by passing the complete pathe. Here iam passing only file name bcz it is in the same folder.
# read n number of file by passing the parameter.
# read function to read the file.
# Readline Function is to read the text by line by line.
# readlines() function stores the lines in textFile to a List and From List it is easy to iterate using for loop.
file = open('textFile.txt')

#print(file.read())
#print(file.read(10))  
#print(file.readline())
#print(file.readline())
#print(file.readline())

#line = file.readline()
#while line != "":
 #   print(line)
  #  line = file.readline()

for line in file.readlines():
    print(line)

file.close  # make sure to close the file.

# Q: print Line by line by using readline.




