class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.nxt
    def addback(self,x):
        t=self.head
        while(t.nxt!=None):
            t=t.nxt
        t.nxt=node(x)
    def midval(self):
        size = 0
        if(self.head):
          t = self.head
          while(t):
            size = size+1
            t=t.nxt
        if size%2==0:
           return "even"
        else:
           return "odd"
l1=sll()
l1.head=node(10)
l1.addback(20)
l1.addback(30)
l1.addback(40)
l1.addback(50)    
l1.addback(60)
l1.addback(70)
l1.addback(80)
l1.display()
print()
l1.midval()
