# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def push(head, x):
	new_node = ListNode(x)
	if head == None:
		head = new_node
	else:
		current = head
		while current.next != None:
			current = current.next
		current.next = new_node

def print_list(head):
	current = head
	while current.next != None:
		current = current.next
		print current.val
	
class Solution:
	# @param head, a ListNode
	# @return a ListNode
	def getTail(self, head):
		cur = head
		while cur.next != None:
			cur = cur.next
		return cur

	def partition(self, head, tail):
		pivot_val = tail.val
		current = head
		less_pivot = head
		first = True
		while current != tail:
			if current.val < pivot_val:
				if first:
					first = False
				else:
					less_pivot = less_pivot.next
				less_pivot.val, current.val = current.val, less_pivot.val
			current = current.next

		less_pivot.next.val, tail.val = tail.val, less_pivot.next.val
		return less_pivot.next

	def quicksort_recur(self, head, tail):
		if head != tail:
			pivot = None
			pivot = self.partition(head, tail)
			
			self.quicksort_recur(head, pivot)
			self.quicksort_recur(pivot.next, tail)
		
	def sortList(self, head):
		self.quicksort_recur(head, self.getTail(head))
		return head
		
def main():
	new_head = ListNode(3)
	push(new_head, 5)
	push(new_head, 20)
	push(new_head, 15)
	push(new_head, 7)
	push(new_head, 6)
	print_list(new_head)
	a = Solution()
	a.sortList(new_head)
	print_list(new_head)
	
if __name__ == '__main__':
	main()
		
			
