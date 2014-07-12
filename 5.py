import pdb
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_list(head):
	current = head
	while current != None:
		print current.val
		current = current.next

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
	def insertionSortList(self, head):
		if head == None or head.next == None:
			return
		cur = head
		while cur != None:
			#print "----------------------------------"
			#print_list(head)
			#pdb.set_trace()
			back = head
			while back != cur:
				if back.val > cur.val:
					while back != cur:
						tmp = cur.val
						back.val, tmp = tmp, back.val
						back = back.next
					break
				back = back.next
			cur = cur.next

		return head

def main():
	a = Solution()
	head = ListNode(3)
	push(head ,15)
	push(head ,5)
	push(head ,4)
	push(head ,1)
	push(head ,2)
	a.insertionSortList(head)
	print "result is"
	print_list(head)

if __name__ == '__main__':
	main()

