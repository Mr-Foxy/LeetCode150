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
