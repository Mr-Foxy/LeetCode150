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
  def zigzagLevelOrder(self, root):
		if not root:
			return []
		res = []
		cur_l = []
		queue = [root]
		head = None
		pdb.set_trace()
		isRev = False
		while queue:
			node = queue[0]
			del queue[0]

			if node == head:
				if isRev:
					cur_l.reverse()
				res.append(cur_l)
				isRev = not isRev
				cur_l = []
				head = None

			cur_l.append(node.val)

			if node.left:
				if not head:
					head = node.left
				queue.append(node.left)

			if node.right:
				if not head:
					head = node.right
				queue.append(node.right)

		if cur_l:
			if isRev:
				cur_l.reverse()
			res.append(cur_l)

		return res

a = Solution()
root = TreeNode(1)
one_1 = TreeNode(2)
one_2 = TreeNode(3)
#two_3 = TreeNode(15)
#two_4 = TreeNode(7)
root.left = one_1
root.right = one_2
#one_2.left = two_3
#one_2.right = two_4
print a.zigzagLevelOrder(root)
