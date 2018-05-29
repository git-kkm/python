# file four.py

print("top-level in four.py")

def func():
    print("func() in four.py")

if __name__ == "__main__":
    print("four.py is being run directly")
else:
    print("four.py is being imported into another module")