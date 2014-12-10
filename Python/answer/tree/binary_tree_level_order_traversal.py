class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root == None:            return []
        
        # In the first stage, we store hte nodes (not their value).
        result = []
        nextLayer = [root]
        
        while len(nextLayer) != 0:
            result.append(nextLayer)
            
            # Gather the nodes in the next deeper layer.
            nextLayer = []
            for father in result[-1]:
                if father.left != None:     nextLayer.append(father.left)
                if father.right != None:    nextLayer.append(father.right)
        
        # In the second stage, we convert the nodes into their values.
        result = [[node.val for node in layer] for layer in result]
        
        return result
