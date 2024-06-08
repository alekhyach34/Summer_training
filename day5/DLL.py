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
    def addfront(self,x):
        if (self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            t.nxt=self.head
            self.head.prev=t
            self.head=t
    def revdisplay(self):
        t = self.tail
        while t != None:
            print(t.data, end="->")
            t = t.prev
        print()
    def linear(self,key):
        p1 = self.head
        p2 = self.tail
        while (p1 != p2 and p1 !=p2.nxt):
            if(p1.data== key or p2.data==key):
                return "found"
            p1=p1.nxt
            p2=p2.prev
        if (p1.data==key):
            return 1
        else:
            return 0
    def evenodd(self):
        s=0
        p1 = self.head
        p2 = self.tail
        while (p1 != p2 and p1 !=p2.nxt):
            p1=p1.nxt
            p2=p2.prev
        if p1==p2:
            return 'even'
        else:
            return 'odd'
    '''def palindrome(self):
        p1=self.head
        if p1 is None:
            return True
        p2 = self.head
        while p2.nxt:
            p2 = p2.nxt
        while p1 != p2:
            if p1.data != p2.data:
                return False
            if p1.nxt == p2:
                break
            p1 = p1.nxt
            p2 = p2.prev
        return True'''
    def palindrome(self):
        p1 = self.head
        p2 = self.tail
        while (p1 != p2 and p1!=p2.nxt):
            if(p1.data!=p2.data):
                return 0
            p1=p1.nxt
            p2=p2.prev
        return 1
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
dl.revdisplay()
print()
print(dl.linear(8))
print()
print(dl.evenodd())
print()
print(dl.palindrome())