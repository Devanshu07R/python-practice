#POLYMORPHISM.....
#Here poly means "many" Polymorphism is a concept in which an object can be treated in many ways it means an object of a class can be used as a object of that derived class#

class A:
    def show(self):
        print("Welcome")

    def show(self):
        print(self, nickname="")

    def show(self, firstname=" "):
        print("Welcome", firstname)

    def show(self, firstname=" ", lastname=" "):
        print("Welcome", firstname, lastname)

    

obj = A()
obj.show()
obj.show("Supriti")
obj.show("Rani")
obj.show("Riya", "Das")