class Solution:
def buildTree(self, inorder, postorder):
  if len(inorder) == 0:
      return None

  postorder_idx = len(postorder)-1
  inorder_idx = len(inorder)-1

  # not strictly a parent stack
  # more of a stack of nodes whose values haven't appeared in
  # inorder yet
  parent = []

  # set initial node
  root = TreeNode(postorder[postorder_idx])
  postorder_idx -= 1

  cur = root
  while postorder_idx >= 0:
      # if we haven't seen the current value in the inorder array
      # then we know that the next node is going to be the right child
      # of the current node
      while cur.val != inorder[inorder_idx]:
          parent.append(cur)
          cur.right = TreeNode(postorder[postorder_idx])
          postorder_idx -= 1
          cur = cur.right

      if postorder_idx < 0:
          break

      inorder_idx -= 1

      # the next root belongs to a left subtree
      # find the correct subtree it belongs to
      while len(parent) > 0 and parent[-1].val == inorder[inorder_idx]:
          inorder_idx -= 1
          cur = parent.pop()

      # finally set the left subtree and continue the reconstruction
      # from there
      cur.left = TreeNode(postorder[postorder_idx])
      postorder_idx -= 1
      cur = cur.left

  return root
