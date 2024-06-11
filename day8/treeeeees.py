class node:
    def _init_(self,u):
        self.data=u
        self.left=None
        self.right=None
class tree:
    def _init_(self):
        self.root=None
    def create(self,root,x):
        if(root==None):
            self.root=node(x)
        elif(root.data>x):
            self.create(root.left,x)
        else:
            self.create(root.right,x)
t1=tree()
t1.create(t1.root,10)
t1.create(t1.root,5)
t1.create(t1.root,20)
t1.create(t1.root,7)
t1.create(t1.root,1)