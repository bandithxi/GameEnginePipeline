import math

class MyVector:
    def __init__(self, xcom = 0, ycom = 0, zcom = 0):
        self.x = xcom
        self.y = ycom
        self.z = zcom

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    
    def mul(self, s):
        return MyVector(self.x * s, self.y * s, self.z * s)

    def div(self, s):
        return MyVector(self.x / float(s), self.y / float(s), self.z / float(s))

    def add(self, opr):
        return MyVector(self.x + opr.x, self.y + opr.y, self.z + opr.z)

    def sub(self, opr):
        return MyVector(self.x - opr.x, self.y - opr.y, self.z - opr.z)

    def __str__(self):
        return 'Vector (' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'

    # Extra Credit problem
    def __add__(self, opr):
       return MyVector(self.x + opr.x, self.y + opr.y, self.z + opr.z)

    def __sub__(self, opr):
        return MyVector(self.x - opr.x, self.y - opr.y, self.z - opr.z)

    def __mul__(self, s):
        return MyVector(self.x * s, self.y * s, self.z * s)

    def __rmul__(self, s):
        return MyVector(self.x * s, self.y * s, self.z * s)

    def __div__(self, s):
        return MyVector(self.x / float(s), self.y / float(s), self.z / float(s))

# Testing
a = MyVector(1.5, 2, 1)
b = MyVector(1, 1, 1)

print "Vector test cases"
print 'a = ' + str(a)
print 'b = ' + str(b)
print 'a.mul(2) = ' + str(a.mul(2))
print 'b.div(2) = ' + str(b.div(2))
print 'a * 2 = ' + str(a * 2)
print '2 * a = ' + str(2 * a)
print 'a / 2.0 = ' +  str(a / 2.0)
print '2.0 / a  = Undefined, can not divide a scalar by a vector\n' 
    
    
        
