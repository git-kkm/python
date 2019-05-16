# coding: utf-8 

mylist = ['Zero', 'One', 'Two', 'Four']
print(mylist)

# append method adds an element to the end of a list. This happens inplace.
mylist.append('Five')
print(mylist)

# insert at index
mylist.insert(3, 'Three')
print(mylist)

# pop method removes an item at the index.
# This method will also return the item you removed from the list.
# If you don’t provide an index, it will by default remove the item at the last index.
print( "pop      : ", mylist.pop())
print( "mylist   : ", mylist)

mylist.remove('Four')
print(mylist)

# The index method returns the first index at which a value occurs.
print( "mylist.index('three') : ", mylist.index('Three'))

list1 = ['Math', 'Physics', 'Chemistry']
list2 = ['History', 'Civics', 'Grography']

list1.extend(list2)
print(list1)
