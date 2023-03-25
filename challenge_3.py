class Student:

    def __init__(self):
        self._name = ""
        self._rollNumber = ""
    
    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name
    
    def getRollNumber(self):
        self._rollNumber

    def setRollNumber(self, rollNumber):
        self._rollNumber = rollNumber

student = Student()
student.setName("Sneha")
student.setRollNumber("2530")
print(student.getName()) #Output:Sneha
print(student.getRollNumber()) #Output:2530





