# Definition for sing# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @return a ListNode
	def addTwoNumbers(self, l1, l2):
		cur1 = l1
		cur2 = l2
		head = None
		curNode = None
		up = 0

		while cur1 and cur2:
			val = cur1.val + cur2.val + up
			up = 0
			if val >= 10:
				up = 1
				val = val % 10
			newNode = ListNode(val)

			if not head:
				head = newNode
				curNode = newNode
			else:
				curNode.next = newNode
				curNode = newNode

			cur1 = cur1.next
			cur2 = cur2.next

		if cur1 or cur2:
			overhead_cur = cur1 if cur1 else cur2
			while overhead_cur:
				val = overhead_cur.val + up
				up = 0
				newNode = ListNode(val % 10)
				if val >= 10:
					up = 1

				if not head:
					head = newNode
					curNode = newNode
				else:
					curNode.next = newNode
					curNode = newNode
				overhead_cur = overhead_cur.next

		if up == 1:
			newNode = ListNode(1)
			curNode.next = newNode

		return head
			
left1 = ListNode(9)
left2 = ListNode(1)
left3 = ListNode(6)

left1.next = left2
left2.next = left3

right1 = ListNode(0)
#right2 = ListNode(6)
#right3 = ListNode(4)

#right1.next = right2
#right2.next = right3

A = Solution()
head = A.addTwoNumbers(left1, right1)

cur = head
while cur:
	print cur.val
	cur = cur.next
