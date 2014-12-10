import pdb
# Definition for singly-linked list.
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
    # @return nothing
		
	def reverse(self, head):
		if head == None:
			return None
		current = head
		nh = head
		while current.next != None:
			tmp = current.next
			current.next = current.next.next
			tmp.next = nh
			nh = tmp
		return nh
			
	def insert(self, inserted_node, prev_node, node):
		prev_node.next = node.next
		node.next = inserted_node.next
		inserted_node.next = node
	
	def get_mid(self, head):
		slow = head
		fast = head
		while fast != None and fast.next != None:
			fast = fast.next.next
			slow = slow.next
		return slow

	def reorderList(self, head):
		if head == None:
			return
		mid = self.get_mid(head)
		reverse_head = mid.next
		mid.next = None
		pdb.set_trace()
		reverse_head = self.reverse(reverse_head)
		
		prev_reversehead = ListNode(-1)
		prev_reversehead.next = reverse_head
		current = head
		print "reverse right half:"
		print_list(reverse_head)
		print "non-reverse left half:"
		print_list(head)
		while reverse_head != None:
			self.insert(current, prev_reversehead, reverse_head)
			reverse_head = prev_reversehead.next
			current = current.next.next

def main():
	head = ListNode(1)
	push(head, 2)
	push(head, 3)
	
	a = Solution()
	a.reorderList(head)
	print "result is :"
	print_list(head)
	
if __name__ == '__main__':
	main()
