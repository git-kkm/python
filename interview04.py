#Lists
my_list = [10, 20, 30, 40]
for i in my_list:
    print(i)

#Tuples
my_tuple = (10, 20, 30, 40)
for i in my_tuple:
    print(i)

#Dict
my_dict = {1:"one", 2:"two", 3:"three"}
for key in my_dict:
    print("key: ", key)

for key, value in my_dict.items(): # For Python 2.x: iteritems
    print("key,value: ", key, value)

#Set
my_set = {1, 2, 3, 1, 2, 3, 4, 1, 2, 3}
for i in my_set:
    print("my_set: ", i)

