# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @param m, an integer
	# @param n, an integer
	# @return a ListNode
	def reverseBetween(self, head, m, n):
		if not head.next or not head:
			return head

		i = 1
		dummy = ListNode(0)
		dummy.next = head
		cur = head
		prev = dummy

		while i != m:	
			cur = cur.next
			prev = prev.next
			i += 1

		prev_start = prev
		start = cur

		prev = prev.next
		cur = cur.next
		while i != n:
			temp = cur.next
			cur.next = prev
			prev = cur
			cur = temp
			i += 1
		prev_start.next = prev
		start.next = cur
		
		return dummy.next

A = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

new_head = A.reverseBetween(node1, 2, 4)
cur = new_head
while cur:
	print cur.val
	cur = cur.next
