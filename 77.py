# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev=None
        current=head
        while (current!= None ):
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        return prev

if __name__=="__main__":
    n = 4
    k = 2
    res=combine(n,k)
    print(res)