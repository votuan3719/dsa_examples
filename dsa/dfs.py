from collections import deque
class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)

# root.left.left = Node(4)
# root.left.right = Node(5)

# root.right.left = Node(6)
# root.right.right = Node(7)

# root.left.left.left = Node(8)
# p = root.left.left.right = Node(9)

# root.left.right.left = Node(10)
# q = root.left.right.right = Node(11)

# root.right.left.left = Node(12)
# root.right.left.right = Node(13)

# root.right.right.left = Node(14)
# root.right.right.right = Node(15)

# root = Node(3)

# root.left = Node(5)
# root.left.left = Node(6)

# root.left.right = Node(2)
# root.left.right.left = Node(7)
# root.left.right.right = Node(4)

# root.right = Node(1)
# root.right.left = Node(0)
# root.right.right = Node(8)

# def traverse(root):
#     queue = deque([root])
    
#     while queue:
#         num_nodes = len(queue)
        
#         for n in range(num_nodes):
#             node = queue.popleft()
            
#             print(node.val)
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)

# traverse(root)

# def lowestCommonAncestor(root: 'Node', p: 'Node', q: 'Node'):
#     queue = deque([root])
#     parent = {root: None}
    
#     while queue:
#         node = queue.popleft()
        
#         if node.left:
#             parent[node.left] = node
#             queue.append(node.left)
#         if node.right:
#             parent[node.right] = node
#             queue.append(node.right)
    
#     ancestors = set()
#     while p:
#         ancestors.add(parent[p])
#         p = parent[p]
    
#     while q not in ancestors:
#         q = parent[q]
    
#     return q

# ans = lowestCommonAncestor(root, p, q)
# print(ans.val)
        
# root = Node(3)

# root.left = Node(9)
# root.right = Node(20)
# root.right.left = Node(15)
# root.right.right = Node(7)

# def minDepth(root):
#     queue = deque([root])
#     depth = 0
    
#     while queue:
#         depth += 1
#         num_nodes = len(queue)
        
#         for _ in range(num_nodes):
#             node = queue.popleft()
            
#             if node.left == None and node.right == None:
#                 return depth
            
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
            
    
#     return depth

# print(minDepth(root))

root = Node(8)
root.left = Node(3)
root.right = Node(10)

root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)

root.left.right.left = Node(4)
root.left.right.right = Node(7)

root.right.right.left = Node(13)

def maxAncestorDiff(root):
    queue = deque([root])
    parent = {root: None}
    
    while queue:
        node = queue.popleft()
        
        if node.left:
            parent[node.left] = node
            queue.append(node.left)
        if node.right:
            parent[node.right] = node
            queue.append(node.right)
    
            

print(maxAncestorDiff(root))

