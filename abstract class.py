from abc import ABC, abstractmethod
class Abclass(ABC):
    def print(self,x):
        print("passed value:",x)
    @abstractmethod
    def task(self):
        print("we are inside Abclass task")
class test_Abclass(Abclass):
    def task(self):
        print("we are inside test class task")
test_obj=test_Abclass()
test_obj.task()
test_obj.print(100)


