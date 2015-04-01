def fact(n = 0, factList = False):
    terms = []
    prod = 1

    for i in range(1, n + 1): 
        prod = prod * i
        if (factList):
            terms.append(prod)
        
    if (factList):
        return (prod, tuple(terms))
    else:
        return prod

class stack: 
    def __init__(self,data=[]):
        self.data = data
    
    def push(self, val):
        self.data.append(val)
    
    def pop(self):
        val = self.data[-1]
        del self.data[-1]
        return val

    def isEmpty(self):
        if self.data:
            return False
        else:
            return True
print fact(4)
myS = stack()
print myS
print myS.isEmpty()
myS.push(1)
myS.push(10)
print myS
print myS.isEmpty()
print myS.pop()
print myS.pop()


def foo(n):
    a, b = 0, 1
    while a < n:
        print a, 
        a, b= b, a+ b

foo(10)
