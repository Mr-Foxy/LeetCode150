import pdb
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
		if not root:
			return 0
			
		stack = []
		stack.append(None)
		top = root
		node_to_n = dict()
		node_to_n[id(root)] = root.val
		res = 0

		while top:
			val = node_to_n[id(top)]
			#pdb.set_trace()
			if not top.left and not top.right:
				res += node_to_n[id(top)]
			if top.right:
				node_to_n[id(top.right)] = val * 10 + top.right.val
				stack.append(top.right)
			if top.left:
				node_to_n[id(top.left)] = val * 10 + top.left.val
				stack.append(top.left)
			top = stack.pop()
			
		return res

root = TreeNode(0)
l = TreeNode(1)
root.left = l
a = Solution()
print a.sumNumbers(root)
