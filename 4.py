class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_list(head):
	cur = head
	while cur != None:
		print cur.val
		cur = cur.next

def push(head, x):
	new_node = ListNode(x)
	if head == None:
		head = new_node
	else:
		current = head
		while current.next != None:
			current = current.next
		current.next = new_node
		
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
		less_pivot = ListNode(-1)
		less_pivot.next = head
		while current != tail:
			if current.val < pivot_val:
				less_pivot = less_pivot.next
				less_pivot.val, current.val = current.val, less_pivot.val
			current = current.next
		less_pivot.next.val, tail.val = tail.val, less_pivot.next.val
			
		return less_pivot, less_pivot.next

	def quicksort_recur(self, head, tail):
		if tail.next == head or tail == head:
			return
		prev, pivot = self.partition(head, tail)
		# for test
		'''
		print "head is {}".format(head.val)
		print "tail is {}".format(tail.val)
		print "pivot is {}".format(pivot.val)
		print_list(head)
		'''
		
		self.quicksort_recur(head, prev)
		if tail != pivot:
			self.quicksort_recur(pivot.next, tail)
		
	def sortList(self, head):
	    if head == None:
	        return None
		self.quicksort_recur(head, self.getTail(head))
		return head
		
def main():
	new_head = ListNode(3)
	'''
	push(new_head, 5)
	push(new_head, 20)
	push(new_head, 15)
	push(new_head, 7)
	push(new_head, 6)
	'''
	a = Solution()
	a.sortList(new_head)
	print "result is :"
	print_list(new_head)
	
if __name__ == '__main__':
	main()
