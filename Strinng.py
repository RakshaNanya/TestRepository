# able to get the substring.

str1 = "RakshananyaAcadedmy.com"
str2 = " is Great"
str3 = "nanya"
print(str1[0])    #0th index of the string
print(str1[0:6])   # Substring i.e Raksha
print(str1[0:6] + str2)   # String cancatanation
print(str3 in str1)  # finding a string present in main string. returns TRUE or FALSE

str4 = str1.split(".")  # splitting a string and we should pass on which parameter string should split.
print(str4)

str5 = " DeadPool "
print(str5)
print(str5.strip())  # trimming blank space from right side of the string
print(str5.lstrip())   # trimming blank space from left side of the string

