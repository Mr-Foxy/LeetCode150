# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
		if not root:
			return 
		queue = []
		queue.append(root)
		i = 1
		j = 0
		while queue:
			node = queue[0]
			del queue[0]
			if i == pow(2,j):
				j += 1
				cur = node
			else:
				cur.next = node
				cur = cur.next
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
			i += 1

