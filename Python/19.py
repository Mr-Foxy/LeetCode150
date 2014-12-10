# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
# @param node, a undirected graph node
# @return a undirected graph node
	def clone_aux(self, new_node, node, traversed):
		traversed[id(node)] = new_node
		for i in node.neighbors:
			if traversed.get(id(i)):
				new_node.neighbors.append(traversed.get(id(i)))
			else:
				new_neighbor = UndirectedGraphNode(i.label)
				new_node.neighbors.append(new_neighbor)
				self.clone_aux(new_neighbor, i, traversed)
		
	def cloneGraph(self, node):
		if not node:
			return None
		traversed = dict()
		new_node = UndirectedGraphNode(node.label)
		self.clone_aux(new_node, node, traversed)
		return new_node

