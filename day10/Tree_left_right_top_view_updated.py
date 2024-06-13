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
    def left_view(self,root,c):
        if root==None:
            return
        if c not in l1:
            l1.append(c)
            print(root.data)
        self.left_view(root.left,c+1)
        self.left_view(root.right,c+1)
    def right_view(self,root,c):
        if root==None:
            return
        if c not in l2:
            l2.append(c)
            print(root.data)
        self.right_view(root.right,c+1)
        self.right_view(root.left,c+1)
    def right_view(self,root,c): #199
        if root==None:
            return
        if c not in l2:
            l2.append(c)
            print(root.data)
        self.right_view(root.right,c+1)
        self.right_view(root.left,c+1)
    def top_view(self,root):
        if root is None:
            return []
        top_view_map = {}
        queue = [(root, 0)]
        while queue:
            node, hd = queue.pop(0)
            if hd not in top_view_map:
                top_view_map[hd] = node.data
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        top_view_list = [top_view_map[hd] for hd in sorted(top_view_map.keys())]
        return top_view_list
    def bottom_view(self,root):
        if root is None:
            return []
        bottom_view_map = {}
        queue = [(root, 0)]
        while queue:
            node, hd = queue.pop(0)
            bottom_view_map[hd] = node.data
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        bottom_view_list = [bottom_view_map[hd] for hd in sorted(bottom_view_map.keys())]
        return bottom_view_list
l1=[]
l2=[]
t1 = Tree()
t1.root = t1.create(t1.root, 10)
t1.root = t1.create(t1.root, 5)
t1.root = t1.create(t1.root, 2)
t1.root = t1.create(t1.root, 20)
t1.root = t1.create(t1.root, 7)
t1.root = t1.create(t1.root, 11)
t1.root = t1.create(t1.root, 4)
t1.root = t1.create(t1.root, 3)
print("Inorder:")
t1.inorder(t1.root)
print("\nPreorder:")
t1.preorder(t1.root)
print("\nPostorder:")
t1.postorder(t1.root)
print("\nleft view:")
t1.left_view(t1.root,0)
print("\nright view:")
t1.right_view(t1.root,0)
print("\ntop view:")
print(t1.top_view(t1.root))
print("\nbottom view:")
print(t1.bottom_view(t1.root))