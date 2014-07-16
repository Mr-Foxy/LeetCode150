# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
		if head == None:
			return None
		new_head = RandomListNode(head.label)
		current = head.next
		new_current = new_head
		while current != None:
			new_node = RandomListNode(current.label)
			new_current.next = new_node
			new_current = new_current.next
			current = current.next


        
