class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        t = self.head
        while t != None:
            print(t.data, end="->")
            t = t.nxt
        print()
    def addback(self,x):
        if (self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            self.tail.nxt=t
            t.prev=self.tail
            self.tail=self.tail.nxt
    def pr(self,t,c):
        if(t==None):
            return c
        def pnt(s,n):
            if(s>=(n//2)+1):
                return 1
            if(n%s==0):
                return 0
            return pnt(s+1,n)
        if(pnt(2,t.data)):
                c=c+1
        self.pr(t.nxt,c)
dl=dll()
dl.head = node(6)
dl.head=dl.tail
dl.addback(7)
dl.addback(4)
dl.addback(8)
dl.addback(4)
dl.addback(2)
dl.addback(0)
dl.addback(1)
dl.display()
print()
print(dl.pnt())
