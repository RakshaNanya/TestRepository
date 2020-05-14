# Create variable in Python
# In python no need to mention the dattatype as in java i.e int string
# no semicolon in python unlike java and c#
# How to print in python
# Concatanation of string
# List DataType supports multiple data with different datatype. i.e int string etc
# index strats with zero in List
# To list we can insert, update, get a substring  and append
# Tuple is similar to List except that a tuple is immutable means we cannot make chnges to the data. Syntax is ()
# Dictonary is a key value pair. Syntax is {}
#
a = 3
print(a)

Var = "Abc"

print(Var)

c, d, e = 1, 32.4, "Hello"
outputC = "The Value of c is "
outputD = "The Value of d is "
print(outputC + str(c))
print(outputD + str(d))

print("{} {} {}".format("The value  of c is ", c , "It is succuss"))
print(e)
print(type(d))

# DataType List

Array = [1, 2, "Raksha", 3]
print(Array)
print("{}{}".format("2nd Index value is ",Array[2]))
# gettingg substring from the list.
print(Array[1:3])

# inserting a data to list
Array.insert(3, "Nanya")
print(Array)
#Updatating the list
Array[2] = "RAKSHA"
print(Array)
#deleting a list

del Array[0]

print(Array)
print(Array[0])

dist = {}
dist["UserID"]= 1
dist["FirstName"] = "Raksha"
dist[1]="user"
print(dist)
