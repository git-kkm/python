# tuple() method can convert list to tuple
# list()  method can convert tuple to list

string2 = "34,67,55,33,12,98"

#Convert String to List
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