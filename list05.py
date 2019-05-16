# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print("Before:" , list_1)
print("Before:" , list_2)

list_1[0] = 'Art'

print("After:" , list_1)
print("After:" , list_2)


# Immutable
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Art'

# print(tuple_1)
# print(tuple_2)

# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

print("cs_courses: ", cs_courses)
