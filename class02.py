# Class variables

class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        #KK we are using the self for raise_amount,
        # so we have both instance and class variable "raise_amount"
        self.pay = int(self.pay * self.raise_amount)


#KK
print('Num of employees: {}' .format(Employee.num_of_emps))

emp_1 = Employee('John', 'Smith', 50000)
emp_2 = Employee('Test','User', 60000)


# emp_1.raise_amount = 1.08  # this updates instances "raise_amount"
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

#KK - This is important.
# Pay attention to the parameters ( instance and class variables printed)
print(emp_1.__dict__)
print(Employee.__dict__)
#KK
print('Num of employees: {}' .format(Employee.num_of_emps))

