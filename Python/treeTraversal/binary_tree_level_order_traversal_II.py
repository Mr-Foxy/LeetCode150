import pdb
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
			queue = [root]
			res = []
			head = None
			cur_level = []
			while queue:
				pdb.set_trace()
				node = queue[0]
				del queue[0]
				if head == node:
					res.append(cur_level)
					cur_level = []
					head = None
				cur_level.append(node.val)

				if node.left:
					if not head:
						head = node.left
					queue.append(node.left)

				if node.right:
					if not head:
						head = node.right
					queue.append(node.right)

			if cur_level:
				res.append(cur_level)

			return res[::-1]
        
a = Solution()
b = TreeNode(1)
c = TreeNode(2)
b.left = c
print a.levelOrderBottom(b)
