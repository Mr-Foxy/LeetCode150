import pdb
# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
	# @param root, a tree node
	# @return a boolean
	def isBalanced(self, root):
		if not root:
			return True
		height, result = self.isBalanced_aux(root)
		return result
	def isBalanced_aux(self, node):
		left_height = 0
		right_height = 0
		left_res = True
		right_res = True

		if not node.left and not node.right:
			return 1, True

		if node.left:
			left_height, left_res =  self.isBalanced_aux(node.left)
		if node.right:
			right_height,right_res = self.isBalanced_aux(node.right)
		
		res_height = 1 + max(left_height, right_height)

		if abs(left_height - right_height) > 1:
			return res_height, False
		else:
			return res_height, left_res and right_res

root = TreeNode(1)
right1 = TreeNode(2)
right2 = TreeNode(3)
root.right = right1
right1.right = right2
a = Solution()
print a.isBalanced(root)
