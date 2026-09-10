
 
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getGpa(self):
        return self.gpa

    def setGpa(self, newGpa):
        if newGpa > 4.0 or newGpa < 0.0:
            print('Invalid new gpa')
        else:
            self.gpa = newGpa

def main():
    s1 = Student('Diego', 3.2)

    s1.setGpa(5.5) # test bad value
    s1.setGpa(3.0)

    print(s1.getName())
    print(s1.getGpa())

main()