from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("Passed value is:",x)
    @abstractmethod
    def task(self):
        print("We are in abstract class")

class test_class(Absclass):
    def task(self):
        print("We are in derived class")

class example_class(Absclass):
    def task(self):
        print("We are in example class")

test_obj = test_class()
test_obj.task()
test_obj.print(100)

ex_obj = example_class()
ex_obj.task()
ex_obj.print(200)

print("test_obj is instance of Absclass?",issubclass(test_class,Absclass))
print("example_obj is instance of Absclass?",issubclass(example_class,Absclass))