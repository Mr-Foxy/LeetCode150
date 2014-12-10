import pdb
# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
      self.val = x
      self.next = None

class Solution:
  # @param head, a ListNode
  # @param k, an integer
  # @return a ListNode
  def reverseKGroup(self, head, k):
		if not head:
			return None
		if k == 1:
			return head

		dummy = ListNode(0)
		dummy.next = head

		prev = dummy
		start = head
		end = head
		
		while True:
			i = 1
			while i < k:
				end = end.next
				i += 1
				if not end:
					return dummy.next
			
			cur = start.next

			lnext = end.next
			while cur != lnext:
				temp = cur.next
				cur.next = start
				start = cur
				cur = temp

			temp = prev.next
			temp.next = cur
			prev.next = end
			
			start = cur
			end = cur
			prev = temp

			if not end:
				break

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

new_head = A.reverseKGroup(node1, 3)

cur = new_head
while cur:
	print cur.val
	cur = cur.next
