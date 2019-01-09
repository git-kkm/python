# if you wans to leave a class empty then use this syntax
class Class01:
    pass

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    def fullname(self):
        return self.first + ' ' + self.last
    def fullname2(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith', 50000)
emp_2 = Employee('Test','User', 60000)

# print(emp_1)
# print(emp_2)

#KK instances variables (or attributes) can be accessed with . and variable name without ()
# methods can be accessed with . and method name and ()
print(emp_1.email)
print(emp_2.email)

# Both the below are the same
print(emp_1.fullname())
print(Employee.fullname(emp_2))

