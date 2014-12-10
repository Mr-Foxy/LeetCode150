# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	# @param a ListNode
	# @return a ListNode
	def swapPairs(self, head):
		if not head:
			return
		dummy = ListNode(0)
		dummy.next = head

		prev = head
		cur = head.next

		temp = dummy

		while cur:
			if temp:
				temp.next = cur
			prev.next = cur.next
			cur.next = prev
			if not prev.next:
				cur = None
			else:
				cur = prev.next.next

			temp = prev
			prev = prev.next

		return dummy.next

A = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

new_head = A.swapPairs(l1)

cur = new_head
while cur:
	print cur.val
	cur = cur.next

