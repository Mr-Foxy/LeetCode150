# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of integers
	def inorderTraversal(self, root):
		if not root:
			return []
		stack = []
		node = root
		res = []
		while stack or node:
			if node:
				stack.append(node)
				node = node.left
			else:
				node = stack.pop()
				res.append(node.val)
				node = node.right
		return res

