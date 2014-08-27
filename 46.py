# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param inorder, a list of integers
	# @param postorder, a list of integers
	# @return a tree node
	def buildTree(self, inorder, postorder):
		length = len(inorder)
		self.buildTree_AUX(inorder, 0, length-1, postorder, 0, length-1)
		return None
	def buildTree_AUX(self, inorder, in_start, in_end, postorder, post_start, post_end):
		if in_start > in_end or post_start > post_end:
			return None
		val = postorder[post_end]
		parent = TreeNode(val)

		for i in range(in_start, in_end+1):
			if inorder[i] == val:
				break

		parent.left = self.buildTree_AUX(inorder, in_start, i-1, postorder, post_start, post_start+i-in_start-1)
		parent.right = self.buildTree_AUX(inorder, i+1, in_end, postorder, post_start+i-in_start, post_end-1)
		return parent

		
        
