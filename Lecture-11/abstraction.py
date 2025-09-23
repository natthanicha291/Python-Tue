from abc import ABC, abstractmethod

class employee(ABC):
    def emp_id(self, id, name, age, salary):
        pass

class childemployee1(employee):
    def emp_id(self, id):
        print("Employee id is 999")

emp = childemployee1()
emp.emp_id(id)