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
    def middle(self):
        f=self.head
        s=self.head
        while(f!=None and f.nxt!=None):
            s=s.nxt
            f=f.nxt.nxt
        self.tail.next=self.head
        self.head.prev=self.tail
        t1=s.prev
        t1.nxt=s.prev
        s.prev=None
        s.head=None
        self.tail=t1
dl=dll()
dl.head = node(3)
dl.head=dl.tail
dl.addback(5)
dl.addback(7)
dl.addback(8)
dl.addback(9)
dl.addback(10)
dl.addback(12)
dl.addback(15)
dl.display()
print()
print(dl.middle())
