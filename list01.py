# tuple() method can convert list to tuple
# list()  method can convert tuple to list

tempList = [30,40,50,60,70,90]

tuple1=tuple(tempList)
print("tuple1: ", tuple1)

list1=list(tuple1)
print("list1: ", list1)

#Convert List to tuple
tuple2=tuple(list1)
print("tuple2: ", tuple2)

print("tuple1 type: ", type(tuple1))
print("list1 type: ", type(list1))
