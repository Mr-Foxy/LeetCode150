class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	# @param num, a list of integers
	# @return a tree node
	def sortedArrayToBST(self, num):
		length = len(num)
		root = self.sortedArrayToBST_aux(num,length)
		return root

	def sortedArrayToBST_aux(self, num, length):
		if length <= 0:
			return None
		mid = (length - 1) / 2
		node = TreeNode(num[mid])
		node.left = self.sortedArrayToBST_aux(num[:mid], mid)
		node.right = self.sortedArrayToBST_aux(num[mid+1:], length / 2)
		return node
	
a = Solution()
res = a.sortedArrayToBST([1,3])
print res.val
print res.right.val
