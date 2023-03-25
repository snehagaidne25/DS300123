class point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):return(self.x* self.x)+(self.y* self.y)+(self.z*self.z)


p = point( 1, 3, 5)

print(p.sqSum())

'''
output:

35
'''


