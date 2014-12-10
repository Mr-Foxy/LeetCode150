# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return an integer
	def maxDepth(self, root):
		return self.maxDepth_AUX(root)
		
	def maxDepth_AUX(self, node):
		if not node:
			return 0

		leftDepth = 1 + self.maxDepth_AUX(node.left)
		rightDepth = 1 + self.maxDepth_AUX(node.right)
		
		return max(leftDepth, rightDepth)
		

