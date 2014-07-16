import pdb
# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

def print_list(head):
	cur = head
	while cur != None:
		print cur.label
		cur = cur.next

def push(head, x):
	new_node = RandomListNode(x)
	if head == None:
		head = new_node
	else:
		current = head
		while current.next != None:
			current = current.next
		current.next = new_node

class Solution:
	# @param head, a RandomListNode
	# @return a RandomListNode
	def copyRandomList(self, head):
		if head == None:
			return None
		cur = head
		next = None
		while cur != None:
			new_node = RandomListNode(cur.label)
			next = cur.next
			cur.next = new_node
			new_node.next = next
			cur = next

		
		cur = head
		while cur != None:
			cur.next.random = cur.random.next if cur.random else None
			cur = cur.next.next

		prev = head
		new_head = head.next
		cur = head.next
		pdb.set_trace()
		while prev != None and prev.next != None:
			prev.next = prev.next.next
			if cur.next != None:
				cur.next = cur.next.next
			prev = prev.next
			cur = cur.next

		print "new List is"
		print_list(new_head)
		print "old list is"
		print_list(head)
		return new_head
			


			

		# My creepy Solution ^
		'''
		if head == None:
			return None
		new_head = RandomListNode(head.label)
		current = head
		new_current = new_head
		current = current.next
		while current != None:
			new_node = RandomListNode(current.label)
			new_node.random = current.random
			new_current.next = new_node

			new_current = new_current.next
			current = current.next

		pdb.set_trace()
		
		current = head
		new_current = new_head
		while current != None:
			current.random = new_current
			current = current.next

		new_current = new_head
		while new_current != None:
			if new_current.random != None:
				new_current.random = new_current.random.random
			new_current = new_current.next

		return new_head
		'''

def main():
	head = RandomListNode(2)
	'''
	push(head, 3)
	push(head, 5)
	push(head, 8)
	push(head, 13)
	push(head, 21)
	'''
	
	a = Solution()
	new_head = a.copyRandomList(head)
	print "result is :"
	print_list(new_head)
	
if __name__ == '__main__':
	main()
