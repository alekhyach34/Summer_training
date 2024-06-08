class node:
    def __init__(self, u):
        self.data = u
        self.nxt = None

class sll:
    def __init__(self):
        self.head = None

    def display(self):
        t = self.head
        while t != None:
            print(t.data, end="->")
            t = t.nxt

    def addback(self, x):
        if not self.head:
            self.head = node(x)
        else:
            t = self.head
            while t.nxt != None:
                t = t.nxt
            t.nxt = node(x)

    def print_all_pairs(self):
        t1 = self.head
        while t1 != None:
            t2 = t1.nxt
            while t2 != None:
                print(f"{t1.data}{t2.data}")
                t2 = t2.nxt
            t1 = t1.nxt
l1 = sll()
l2 = sll()

l1.head = node(6)
l1.addback(7)
l1.addback(4)
l1.addback(8)
l1.addback(4)
l1.addback(2)
l1.addback(0)
l1.addback(1)
l1.display()
print()
l1.print_all_pairs()
