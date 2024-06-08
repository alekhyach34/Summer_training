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
    def is_balanced(self):
        stack=[]
        t=self.head
        index=1
        while t is not None:
            if t.data=='(' or t.data=='[' or t.data=='{':
                stack.append((t.data,index))
            elif t.data==')' or t.data==']' or t.data=='}':
                if not stack:
                    print(index)
                    return
                top,top_index=stack.pop()
                if(top=='(' and t.data!=')') or  (top=='[' and t.data!=']') or (top=='{' and t.data!='}'):
                    print(index)
                    return
            t=t.nxt
            index+=1
        if stack:
            top_index=stack.pop()
            print(top_index)
        else:
            print(-1)
dl=dll()
dl.head = node('[')
dl.head=dl.tail
dl.addback('[')
dl.addback('{')
dl.addback('{')
dl.addback(')')
dl.addback(']')
dl.display()
print()
dl.is_balanced()
