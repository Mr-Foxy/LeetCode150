# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
  # @param two ListNodes
  # @return a ListNode
  def mergeTwoLists(self, l1, l2):
		res = ListNode(0) 
		cur = res
		cur_l1 = l1
		cur_l2 = l2
		new_node = None
		while cur_l1 and cur_l2:
			if cur_l1.val < cur_l2.val:
				new_node = ListNode(cur_l1.val)
				cur.next = new_node
				cur = cur.next
				cur_l1 = cur_l1.next
			else:
				new_node = ListNode(cur_l2.val)
				cur.next = new_node
				cur = cur.next
				cur_l2 = cur_l2.next
			
		if cur_l1:
			while cur_l1:
				new_node = ListNode(cur_l1.val)
				cur.next = new_node
				cur = cur.next
				cur_l1 = cur_l1.next

		if cur_l2:
			while cur_l2:
				new_node = ListNode(cur_l2.val)
				cur.next = new_node
				cur = cur.next
				cur_l2 = cur_l2.next

		return res.next
				

A = Solution()
print A.mergeTwoLists([1,4,7,9,12], [2])

'''
			i = 0
			j = 0
			l1_len = len(l1)
			l2_len = len(l2)
			res = []
			while i < l1_len and j < l2_len:
				if l1[i] < l2[j]:
					res.append(l1[i])
					i += 1
				else:
					res.append(l2[j])
					j += 1

			if i == l1_len:
				for k in range(j, l2_len):
					res.append(l2[k])

			if j == l2_len:
				for k in range(i, l1_len):
					res.append(l1[k])

			return res
'''
