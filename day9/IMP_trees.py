class Node:
    def __init__(self, u):
        self.data=u
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root = None
    def create(self, root, x):
        if root is None:
            return Node(x)
        elif root.data > x:
            root.left = self.create(root.left, x)
        else:
            root.right = self.create(root.right, x)
        return root
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data, end=",")
            self.inorder(root.right)
    def preorder(self,root):
        if root:
            print(root.data, end=",")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=",")
    #ADDING TREE NODES
    def addtree(self,root):
        if root==None:
            return 0
        return root.data + self.addtree(root.left)+ self.addtree(root.right)
    def evensum(self,root):
        es=0
        if root==None:
            return 0
        if root.data%2==0:
            es=es+root.data
            return es + self.evensum(root.left)+ self.evensum(root.right)
        return self.evensum(root.left)+ self.evensum(root.right)
    def evod_diff(self,root):
        if root==None:
           return 0
        if (root.data%2==0):
           return root.data + self.evod_diff(root.left)+ self.evod_diff(root.right)
        return self.evod_diff(root.left)+ self.evod_diff(root.right) - root.data
    def treeh(self,root):
        m=0
        if root==None:
           return -1
        return max(self.treeh(root.left),self.treeh(root.right))+1
    def bal(self,root):
        return abs(self.treeh(root.left)-self.treeh(root.right))<=1
    def countleaf(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        return self.countleaf(root.left) + self.countleaf(root.right)  
    def leafnodes(self,root):
        if root==None:
            return 0
        elif root.left==None and root.right==None:
            return root.data 
        return self.leafnodes(root.left) + self.leafnodes(root.right)
    def search(self,root,key):
        if root== None:
            return 0    #
        if key==root.data:
            return 1
        elif key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)
    def depth(self,root,y,c):
        if root==None:
           return -1
        if root.data==y:
            return c
        if root.data>y:
            return self.depth(root.left,y,c+1)
        else:
            return self.depth(root.right,y,c+1)
t1 = Tree()
t1.root = t1.create(t1.root, 10)
t1.root = t1.create(t1.root, 5)
t1.root = t1.create(t1.root, 2)
t1.root = t1.create(t1.root, 20)
t1.root = t1.create(t1.root, 7)
t1.root = t1.create(t1.root, 1)
print("Inorder:")
t1.inorder(t1.root)
print("\nPreorder:")
t1.preorder(t1.root)
print("\nPostorder:")
t1.postorder(t1.root)
print("\naddtree:")
print(t1.addtree(t1.root))
print("\naddtree left:")
print(t1.addtree(t1.root.left))
print("\naddtree right:")
print(t1.addtree(t1.root.right))
print("\ndifference of tree:")
print(abs(t1.addtree(t1.root.left)-t1.addtree(t1.root.right)))
print("\neven sum:")
print(t1.evensum(t1.root))
print("\neven diff:")
print(t1.evod_diff(t1.root))
print("\ntree height:")
print(t1.treeh(t1.root))
print("\nbalanced or not:")
if t1.bal(t1.root):
    print('bal')
else:
    print('not bal')
print('\ncount leaf node')
print(t1.countleaf(t1.root))
print('\nleaf node')
print(t1.leafnodes(t1.root))
print('\nsearch')
key= 4
if t1.search(t1.root,key):
    print("key is present in the tree.")
else:
    print("key is not found in the tree.")
print('\ndepth')
print(t1.depth(t1.root,20,0))