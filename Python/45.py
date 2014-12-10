# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of lists of integers
	def levelOrderBottom(self, root):
		if not root:	
			return []
		queue = []
		queue.append(root)
		head = None
		res = []
		cur_level = []
		while queue:
			node = queue[0]
			del queue[0]

			if node == head:
				res.append(cur_level)
				head = None
				cur_level = []
			
			cur_level.append(node.val)

			if node.left:
				if not head:
					head = node.left
				queue.append(node.left)

			if node.right:
				if not head:
					head = node.right
				queue.append(node.right)
		res.append(cur_level)

		return res[::-1]

root = TreeNode(1)
a = Solution()
print a.levelOrderBottom(root)
