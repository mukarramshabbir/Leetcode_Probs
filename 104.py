from collections import deque
#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    queue=deque([(root,1)])
    while queue:
        node,depth=queue.popleft()
        if node.left:
            queue.append((node.left,depth+1))
        if node.right:
            queue.append((node.right, depth + 1))
    return depth
                
    
if __name__=="__main__":
    # Example usage
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    depth = maxDepth(root)
    print("Maximum depth:", depth)  # Output: Maximum depth: 3