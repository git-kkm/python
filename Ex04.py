# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# tuple() method can convert list to tuple

tempList = [30,40,50,60,70,90]

tuple1 = tuple(tempList)
print('tuple1: ', tuple1)

list1=list(tuple1)
print("list1: ", list1)

print("-----------------------------------------------")

string2 = "34,67,55,33,12,98"

####Convert String to List
list2 = string2.split(",")
print("list2: ", list2)

####Convert List to tuple
tuple2=tuple(list2)
print("tuple2: ", tuple2)

####Convert tuple to List
list3=list(tuple2)
print("list3: ", list3)

print("-----------------------------------------------")

print("string2 type: ", type(string2))
print("tuple2 type: ", type(tuple2))
print("list2 type: ", type(list2))
print("-----------------------------------------------")