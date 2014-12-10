# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
			if not root:
				return []
			queue = [root]
			head = None
			res = []
			c_lev = []
			while queue:
				node = queue[0]
				del queue[0]
				if head == node:
					res.append(c_lev)
					c_lev = []
					head = None
				c_lev.append(node.val)

				if node.left:
					if not head:
						head = node.left
					queue.append(node.left)

				if node.right:
					if not head:
						head = node.right
					queue.append(node.right)

			if c_lev:
				res.append(c_lev)

				return res
