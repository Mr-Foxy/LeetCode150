# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
		result = []
		stack = []

		if root == None:
			return result
		stack.append(None)
		top = root
		while top != None:
			result.append(top.val)
			if top.right != None:
				stack.append(top.right)
			if top.left != None:
				stack.append(top.left)
			top = stack.pop()
		return result
