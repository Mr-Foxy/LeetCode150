# Definition for a  binary tree node
#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
	# @param root, a tree node
	# @return nothing, do it in place
	def flatten(self, root):
		if not root:
			return
		stack = [None]
		node_list = []
		node = root
		while node:
			node_list.append(node)
			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)
			node = stack.pop()
			
		for i in node_list:
			print i.val
		len_list = len(node_list)
		for i in range(len_list - 1):
			node_list[i].left = None
			node_list[i].right = node_list[i+1]

		node_list[-1].left = None
		node_list[-1].right = None

#root = TreeNode(1)
#left = TreeNode(2)
#root.left = left
#a = Solution()
#a.flatten(root)
			
        
