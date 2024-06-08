'''#Linked list for adding nodes
class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def display(self):
        t=head
        while(t!=None):
            print(t.data)
            t=t.nxt
l1=sll()
head=node(10)
head.nxt=node(20)
head.nxt.nxt=node(30)
head.nxt.nxt.nxt=node(40)
l1.display()

#sum of those nodes
class node:
    def _init_(self,u):
        self.data=u
        self.nxt=None
class sll:
    def display(self):
        t=head
        s=0
        while(t!=None):
            s=s+t.data
            t=t.nxt
        print(s)
l1=sll()
head=node(10)
head.nxt=node(20)
head.nxt.nxt=node(30)
head.nxt.nxt.nxt=node(40)
l1.display()

#adding node at end
class node:
    def _init_(self,u):
        self.data=u
        self.nxt=None
class sll:
    def display(self):
        t=head
        while(t!=None):
            print(t.data)
            t=t.nxt
    def addback(self,x):
        t=head
        while(t.nxt!=None):
            t=t.nxt
        t.nxt=node(x)
l1=sll()
head=node(10)
l1.addback(20)
l1.addback(30)
l1.addback(40)
l1.addback(50)    
l1.display()

#2 linked list in same program
class node:
    def _init_(self,u):
        self.data=u
        self.nxt=None
class sll:
    def _init_(self):
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
l1=sll()
l2=sll()
l1.head=node(10)
l1.addback(20)
l1.addback(30)
l1.addback(40)
l1.addback(50)    
l1.display()
l2.head=node(100)
l2.addback(200)
l2.addback(300)
print()
l2.display()
'''
#add even numbers in linked list
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
    def addeven(self):
        t=self.head
        s=0
        while(t!=None):
            if(t.data%2==0):
                s=s+t.data
        print(s)
l1=sll()
l2=sll()
l1.head=node(10)
l1.addback(20)
l1.addback(30)
l1.addback(40)
l1.addback(50)    
l2.head=node(100)
l2.addback(200)
l2.addback(300)
l1.display()
print()
l2.display()
print()
l1.addeven()
print()
l2.addeven()
