# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	# @param preorder, a list of integers
	# @param inorder, a list of integers
	# @return a tree node
	def buildTree(self, preorder, inorder):
		length = len(preorder)
		return self.buildTree_AUX(preorder, 0, length-1, inorder, 0, length-1)
	
	def buildTree_AUX(self, preorder, pre_start, pre_end, inorder, in_start, in_end):
		if pre_start > pre_end or in_start > in_end:
			return None

		val = preorder[pre_start]
		parent = TreeNode(val)
		for i in range(in_start, in_end+1):
			if val == inorder[i]:
				break

		parent.left = self.buildTree_AUX(preorder, pre_start+1, pre_start+i-in_start, inorder, in_start, i-1)
		parent.right = self.buildTree_AUX(preorder, pre_start+i-in_start+1, pre_end, inorder, i+1, in_end)
		return parent
