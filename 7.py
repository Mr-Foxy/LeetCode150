import pdb
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
		node = root
		stack = []
		result = []
		last_visited = None
		while node != None or len(stack) != 0:
			pdb.set_trace()
			if node != None:
				stack.append(node)
				node = node.left
			else:
				peek_node = stack[-1]
				if peek_node.right != None and peek_node.right != last_visited:
					node = peek_node.right
				else:
					result.append(stack.pop().val)
					last_visited = peek_node

		return result


def main():
	root = TreeNode(1)
	a = Solution()
	a.postorderTraversal(root)

if __name__ == '__main__':
	main()
	
        
