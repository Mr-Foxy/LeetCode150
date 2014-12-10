# Definition for a  binary tree node
# class TreeNode
#     def __init__(self, x)
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  # @param root, a tree node
  # @return a boolean
  def isSymmetric(self, root):
		if not root:
			return True
		leftqueue = [root]
		rightqueue = [root]
		
		while leftqueue:
			leftNode = leftqueue.pop(0)
			rightNode = rightqueue.pop(0)
			
			if leftNode.left:
				if not rightNode.right:
					return False
				if rightNode.right.val != leftNode.left.val:
					return False
				leftqueue.append(leftNode.left)
				rightqueue.append(rightNode.right)

			if leftNode.right:
				if not rightNode.left:
					return False
				if rightNode.left.val != leftNode.right.val:
					return False
				leftqueue.append(leftNode.right)
				rightqueue.append(rightNode.left)

		return True
