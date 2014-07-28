# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
			if not root:
				return 
			queue = []
			queue.append(root)
			cur_level = 1
			next_level = 0
			i = 0
			cur = root
			while queue:
				node = queue[0]
				del queue[0]
				if i == cur_level:
					cur_level = next_level
					next_level = 0
					cur = node
					i = 0
				else:
					cur.next = node
					cur = cur.next
				if node.left:
					queue.append(node.left)
					next_level += 1
				if node.right:
					queue.append(node.right)
					next_level += 1
				i += 1



