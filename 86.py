from collections import deque
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less_head = ListNode(0)
        less = less_head
        greater_head = ListNode(0)
        greater = greater_head
    
        current = head
    
        while current:
            if current.val < x:
                # Append the node to the less than x partition
                less.next = current
                less = less.next
            else:
                # Append the node to the greater than or equal to x partition
                greater.next = current
                greater = greater.next
    
            current = current.next
    
        # Connect the two partitions
        less.next = greater_head.next
        greater.next = None  # Set the end of the greater partition to None to avoid cycles
    
        return less_head.next

    
if __name__=="__main__":
    # Example usage
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    depth = maxDepth(root)
    print("Maximum depth:", depth)  # Output: Maximum depth: 3