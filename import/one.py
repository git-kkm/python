# file one.py
import two


'''
import folder1.three

print("top-level in one.py")

two.func()
folder1.three.func()
'''


'''
from folder1 import three

print("top-level in one.py")

two.func()
three.func()
'''


'''
import two
import folder1.three
import folder1.folder2.four

print("top-level in one.py")

two.func()
folder1.three.func()
folder1.folder2.four.func()
'''



import two
from folder1 import three
from folder1.folder2 import four

print("top-level in one.py")

two.func()
three.func()
four.func()



if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")
    