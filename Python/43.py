import pdb
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	# @param head, a list node
	# @return a tree node
	def sortedListToBST(self, head):
		cur = head
		count = 0
		while cur:
			count += 1
			cur=cur.next
		#print count
		l = self.sortedListToBST_aux(head, 0, count-1)
		return l[0]
		#pdb.set_trace()
	
	def sortedListToBST_aux(self, cur_list, start, end):
		#pdb.set_trace()
		if start > end:
			return None, cur_list
		mid = start + (end - start) / 2
		left_child, cur = self.sortedListToBST_aux(cur_list, start, mid-1)
		parent = TreeNode(cur.val)
		parent.left = left_child
		cur = cur.next
		parent.right, cur = self.sortedListToBST_aux(cur, mid+1, end)
		return parent, cur
		
head = ListNode(1)
next = ListNode(3)
head.next = next
a = Solution()
a.sortedListToBST(head)


