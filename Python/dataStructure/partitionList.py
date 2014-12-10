import pdb
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @param x, an integer
	# @return a ListNode
	def partition(self, head, x):
		if not head:
			return head
		
		dummy = ListNode(-1)
		dummy.next = head

		i = dummy
		j = head
		prev = dummy

		while j:
			c = dummy.next
			#while c:
			#	print c.val
			#	c = c.next
			pdb.set_trace()

			if j.val < x:
				i = i.next
				if i == j:
					prev = prev.next
					j = j.next
					continue
				# Tou Tian Huan Ri
				j_nextNode = j.next
				i_nextNode = i.next
				j.next = i_nextNode
				prev.next = j_nextNode
				i.next = j
				j = j_nextNode
			else:
				j = j.next
				prev = prev.next
		return dummy.next

A = Solution()
node1 = ListNode(2)
node2 = ListNode(1)
#node3 = ListNode(3)
#node4 = ListNode(2)
#node5 = ListNode(5)
#node6 = ListNode(2)

node1.next = node2
#node2.next = node3
#node3.next = node4
#node4.next = node5
#node5.next = node6

A.partition(node1, 2)

cur = node1
while cur:
	print cur.val
	cur = cur.next

''' 
		Theta(N) Space Complexity, which is creepy -_-

		queue_small = []
		queue_large = []

		cur = head
		while cur:
			if cur.val >= x:
				queue_large.append(cur.val)
			else:
				queue_small.append(cur.val)
			cur = cur.next
			
		cur = head
		while queue_small:
			cur.val = queue_small.pop(0)
			cur = cur.next
		
		while queue_large:
			cur.val = queue_large.pop(0)
			cur = cur.next

		return head
'''

