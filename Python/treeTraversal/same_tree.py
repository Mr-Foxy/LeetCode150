# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
  # @param p, a tree node
  # @param q, a tree node
  # @return a boolean
  def isSameTree(self, p, q):
		if not p and not q:	
			return True
		if (not p and q) or (not q and p):
			return False
		queue1 = [p]
		queue2 = [q]
		node1 = None
		node2 = None
		while queue1 and queue2:
			node1 = queue1[0]
			del queue1[0]
			node2 = queue2[0]
			del queue2[0]
			if node1.val != node2.val:
				return False
			if node1.left:
				if not node2.left:
					return False
				queue1.append(node1.left)
			if node2.left:
				if not node1.left:
					return False
				queue2.append(node2.left)
			if node1.right:
				if not node2.right:
					return False
				queue1.append(node1.right)
			if node2.right:
				if not node1.right:
					return False
				queue2.append(node2.right)
		if queue1 or queue2:
			return False
		return True

a = Solution()
root1 = TreeNode(1)
left1 = TreeNode(0)
root1.right = left1
root2 = TreeNode(1)
left2 = TreeNode(0)
root2.right = left2
print a.isSameTree(root1, root2)
