# Definition for a  binary tree node 
class TreeNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	# @param root, a tree node
	# @return an integer
	def maxDepth(self, root):
		if not root:
			return 0
		return self.maxDepth_AUX(root)

		
	def maxDepth_AUX(self, node):
		if not node.left and not node.right:
			return 1
		right = 0
		left = 0
		if node.left:
			left = self.maxDepth_AUX(node.left) + 1
		if node.right:
			right = self.maxDepth_AUX(node.right) + 1
		return max(left, right)

root = TreeNode(1)
left = TreeNode(2)
root.left = left
a = Solution()
print a.maxDepth(root)
