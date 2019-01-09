string1 = "34,67,55,33,12,98"

# Convert string to List (where each member is a string)
list1 = string1.split(",")
print("list1 : ", list1)


# CONVERT list to string.
# values should be a sequence of strings.
string2 = ",".join(list1)
print("string2 : ", string2)

print("string1 type: ", type(string1))
print("list1 type: ", type(list1))

