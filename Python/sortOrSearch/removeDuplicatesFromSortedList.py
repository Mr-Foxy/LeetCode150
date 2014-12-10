# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
  # @param head, a ListNode
  # @return a ListNode
  def deleteDuplicates(self, head):
		if not head:
			return None

		prev = head
		cur = head.next
		val = head.val
		while cur:
			if cur.val == val:
				prev.next = cur.next
			else:
				val = cur.val
				prev = prev.next
			cur = cur.next

		return head

a = Solution()
one = ListNode(1)
two = ListNode(1)
three = ListNode(1) 
#four = ListNode(3)
one.next = two
two.next = three
#three.next = four
cur = one
new = a.deleteDuplicates(one)
cur = new
while cur:
	print cur.val
	cur = cur.next
