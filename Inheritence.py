#INHERITENCE
#Inheritence allows a class to inherit the properties and behaviour from the another class, basically the base class inherits the properties from the derive class...#

class Father:
    def lands(self):
        print("having 200 acres of land.")

class Son(Father):
    def properties(self):
        print("Want to plot a house rate 56 lakhs...")

S=Son()
S.lands()
S.properties()