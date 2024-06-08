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
    def pair_swap(self):
        if not self.head or not self.head.nxt:
            return
        t=self.head
        self.head=t.nxt 
        while t and t.nxt:
            t1=t.nxt
            t3=t1.nxt
            t1.nxt=t
            t1.prev=t.prev
            t.nxt=t3
            t.prev=t1
            if t3:
                t3.prev=t
            if t1.prev:
                t1.prev.nxt=t1
            t=t3
dl=dll()
dl.head = node(3)
dl.head=dl.tail
dl.addback(5)
dl.addback(7)
dl.addback(8)
dl.addback(9)
dl.display()
print()
dl.pair_swap()
dl.display()
