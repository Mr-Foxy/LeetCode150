# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
		node = root
		stack = []
		last_visit = None
		s_v_set = dict()
		max_value = -1
		while stack or node:
			if node:
				stack.append(node)
				node = node.left
			else:
				peek_node = stack[-1]
				if peek_node.right and last_visit != peek_node.right:
					node = peek_node.right
				else:
					stack.pop()
					s_v_set[id(peek_node)] = peek_node.val + max(s_v_set.get(id(peek_node.left), 0), s_v_set.get(id(peek_node.right), 0))
					max_value = max(max_value, peek_node.val + s_v_set.get(id(peek_node.left), 0) + s_v_set.get(id(peek_node.right), 0))
					last_visit = peek_node
		return max_value
    
