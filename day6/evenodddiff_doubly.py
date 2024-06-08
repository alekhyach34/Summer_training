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
    '''def diff_evensum_oddsum(self):
        t=self.head
        s1,s2=0,0
        while(t!=None):
            if(t.data%2==0):
                s1=s1+t.data
            elif(t.data%2!=0):
                s2=s2+t.data
            t=t.nxt
            d=abs(s1-s2)
        print(d)
    def diff_evensum_oddsum_recursive(self, t, s1, s2):
        if t is None:
            return abs(s1 - s2)
        if t.data % 2 == 0:
            s1 += t.data
        else:
            s2 += t.data
        return self.diff_evensum_oddsum_recursive(t.nxt, s1, s2)
    def diff_evensum_oddsum(self):
        return self.diff_evensum_oddsum_recursive(self.head, 0, 0)
    def even_odd_sum(self):
        def recur(x):
            if x is None:
                return 0,0
            ev,odd=recur(x.nxt)
            if x.data%2==0:
                ev+=x.data
            else:
                odd+=x.data
            return ev,odd
        ev,odd=recur(self.head)
        return abs(ev-odd)
    def evod(self,t,es,os):
        if(t==None):
            return 
        if(t.data%2==0):
            es=es+t.data
        else:
            os=os+t.data
        return self.evod(t.nxt,es,os)'''
    def is_prime(self, node, divisor=2):
        c=0
        if number < 2:
            return False
        if divisor * divisor > number:
            return True
        elif number % divisor == 0:
            return False
        else:
            self.is_prime(number, divisor + 1)
            c+=1
        return self.is_prime(node.nxt,2)
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
print(dl.is_prime())
