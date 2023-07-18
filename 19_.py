class ListNode:
    def __init__(self,val=0,next=None) -> None:
        self.val=val
        self.next=next

def removeNthFromEnd( head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    # Create a dummy node to handle edge cases where the head needs to be removed
    dummy = ListNode(0)
    dummy.next = head
    
    # Initialize two pointers, slow and fast, both pointing to the dummy node
    slow = fast = dummy
    
    # Move the fast pointer n+1 positions ahead
    for _ in range(n + 1):
        fast = fast.next
    
    # Move the slow and fast pointers simultaneously until the fast pointer reaches the end
    while fast:
        slow = slow.next
        fast = fast.next
    
    # Remove the nth node from the end by updating the pointers
    slow.next = slow.next.next
    
    # Return the updated head (dummy.next) of the linked list
    return dummy.next
        
            
    

if __name__=="__main__":
    head = [1,2,3,4,5]
    n = 2
    result = removeNthFromEnd(head,n)
    print(result)