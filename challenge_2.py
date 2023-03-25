class Calculator:
    def __init__(self,num1,num2):

        self.num1 = num1
        self.num2 = num2

    def add(self):
        return (self. num2 + self. num1)

    def sub(self):
        return (self. num2 - self.num1)
    
    def mul(self):
        return (self. num2 / self.num1)
    
    
s1 = Calculator(10, 94)
print(s1.add())
print(s1.sub())
print(s1.mul())
print(s1.div())

'''
Output:

104
84
9.4

'''


