'''class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def left_view_recursive(root, result=[], level=0):
    if not root:
        return
    if level == len(result):
        result.append(root.val)
    left_view_recursive(root.left, result, level + 1)
    left_view_recursive(root.right, result, level + 1)
    return result
def right_view_recursive(root, result=[], level=0):
    if not root:
        return
    if level == len(result):
        result.append(root.val)
    right_view_recursive(root.right, result, level + 1)
    right_view_recursive(root.left, result, level + 1)
    return result
def top_view(root):
    if not root:
        return
    queue = [(root, 0)]  
    top_nodes = {}
    while queue:
        node, hd = queue.pop(0)
        if hd not in top_nodes:
            top_nodes[hd] = node.val
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    for hd in sorted(top_nodes):
        print(top_nodes[hd], end=" ")
def bottom_view(root):
    if not root:
        return
    queue = [(root, 0)]  
    bottom_nodes = {}
    while queue:
        node, hd = queue.pop(0)
        bottom_nodes[hd] = node.val
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    for hd in sorted(bottom_nodes):
        print(bottom_nodes[hd], end=" ")

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.left.left.left = TreeNode(1)
root.left.left.right = TreeNode(3)

print("\nLeft view:")
print(left_view_recursive(root))
print("\nBottom view:")
bottom_view(root)
print("\nRight view:")
print(right_view_recursive(root))
print("\nTop view:")
top_view(root)


'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def left_view_recursive(root, result=[], level=0):
    if not root:
        return
    if level == len(result):
        result.append(root.val)
    left_view_recursive(root.left, result, level + 1)
    left_view_recursive(root.right, result, level + 1)
    return result

def right_view_recursive(root, result=[], level=0):
    if not root:
        return
    if level == len(result):
        result.append(root.val)
    right_view_recursive(root.right, result, level + 1)
    right_view_recursive(root.left, result, level + 1)
    return result

def top_view(root, hd=0, top_nodes={}):
    if not root:
        return
    if hd not in top_nodes:
        top_nodes[hd] = root.val
    top_view(root.left, hd - 1, top_nodes)
    top_view(root.right, hd + 1, top_nodes)

def bottom_view(root, hd=0, bottom_nodes={}):
    if not root:
        return
    bottom_nodes[hd] = root.val
    bottom_view(root.left, hd - 1, bottom_nodes)
    bottom_view(root.right, hd + 1, bottom_nodes)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.left.left.left = TreeNode(1)
root.left.left.right = TreeNode(3)

print("Left view:")
print(left_view_recursive(root))
print("\nBottom view:")
bottom_view(root)
for hd in sorted(bottom_view):
    print(bottom_view[hd], end=" ")
print("\nRight view:")
print(right_view_recursive(root))
print("\nTop view:")
top_view(root)
for hd in sorted(top_view):
    print(top_view[hd], end=" ")
