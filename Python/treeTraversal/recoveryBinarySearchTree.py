# Definition for a  binary tree node
#class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	def __init__(self):
		self.m_firstNode = None
		self.m_secondNode = None
		self.m_prevElement = TreeNode(-0x3f3f3f3f)

	def recoverTree(self, root):
		# self.inorderTraversal(root)
		return self.morrisTraversal(root)

	def inorderTraversal(self, root):
		if not root:
			return root
		
		stack = []
		curNode = root
		popedNode = None

		firstNode = None
		secondNode = None
		prevNode = TreeNode(-0x3f3f3f3f) 

		while stack or curNode:
			if curNode:
				stack.append(curNode)
				curNode = curNode.left
			else:
				popedNode = stack.pop()
				if popedNode.val <= prevNode.val and not firstNode:
					firstNode = prevNode

				if popedNode.val <= prevNode.val and firstNode:
					secondNode = popedNode

				prevNode = popedNode
				curNode = popedNode.right

		firstNode.val, secondNode.val = secondNode.val, firstNode.val

		return root
	
	def morrisTraversal(self, root):	
		cur = root

		while cur != None:
			if not cur.left:
				self.findErrorElement(cur)
				cur = cur.right
			else:
				pre = cur.left
				while pre.right and pre.right != cur:
					pre = pre.right

				if not pre.right:
					pre.right = cur
					cur = cur.left
					
				if pre.right == cur:
					self.findErrorElement(cur)
					pre.right = None
					cur = cur.right
		
		self.m_firstNode.val, self.m_secondNode.val = self.m_secondNode.val, self.m_firstNode.val
		return root
		
	def findErrorElement(self, cur):
		if cur.val <= self.m_prevElement.val and not self.m_firstNode:
			self.m_firstNode = self.m_prevElement

		if cur.val <= self.m_prevElement.val and self.m_firstNode:
			self.m_secondNode = cur

		self.m_prevElement = cur
