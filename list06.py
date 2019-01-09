list_1 = ['History', 'Math', 'Physics', 'CompSci']
print(list_1)

list_1.append('Biology')
print(list_1)

list_1.remove('History')
print(list_1)

# insert at index
list_1.insert(1, 'Geography')
print(list_1)


courses   = ['Math', 'Physics', 'Chemistry']
courses_2 = ['History', 'Civics', 'Grography']

courses.extend(courses_2)
print(courses)
