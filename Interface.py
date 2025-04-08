from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def show(self):
        pass
    class Square(Shape):
        def show(self):
          print("Square has 4 sides...")

    class Circle(Shape):
        def show(self):
           print("Circle has no sides, Circle has Circle shape...")

S= Square()
S.show()
C= Circle()
C.show()

