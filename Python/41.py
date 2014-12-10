# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
			if not root:
				return 0
			queue = [root]
			head = None
			level = 1
			while queue:
				node = queue[0]
				del queue[0]
				
				if node == head:
					level += 1
					head = None

				if not node.left and not node.right:
					return level

				if node.left:
					if not head:
						head = node.left
					queue.append(node.left)
					
				if node.right:
					if not head:
						head = node.right
					queue.append(node.right)


        
