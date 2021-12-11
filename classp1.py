x=int(input())
n=int(input())
class number:
    def __init__(self,x,n):
        self.x=x
        self.n=n
    def power(self):
        p=self.x**self.n
        return p
o1=number(x,n)
print(o1.power())
