# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
			if not root:
				return []

			queue = []
			queue.append(root)
			node_val = dict()
			node_path = dict()
			node_val[id(root)] = root.val
			node_path[id(root)] = [root.val]
			res = []
			while queue:
				node = queue[0]
				del queue[0]

				val = node_val[id(node)]
				path = node_path[id(node)]
				if not node.left and not node.right:
					if val == sum:
						res.append(path)
				if node.left:
					node_val[id(node.left)] = val + node.left.val
					node_path[id(node.left)] = path + [node.left.val]
				if node.right:
					node_val[id(node.right)] = val + node.right.val
					node_path[id(node.right)] = path + [node.right.val]
				
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right) 

			return res
