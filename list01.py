# coding: utf-8 

# tuple() method can convert list to tuple
# list()  method can convert tuple to list

list1 = [30,40,50,60,70,90]

#Convert List to tuple
tuple1 = tuple(list1)
print("tuple1: ", tuple1)

list2 = list(tuple1)
print("list2: ", list2)

print("list2 type: ", type(list2))
print("tuple1 type: ", type(tuple1))
