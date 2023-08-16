# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1=l1.next
        while l2:
            stack2.append(l2.val)
            l2=l2.next
        carry=0
        result=None
        while stack1 or stack2 or carry:
            val1=stack1.pop() if stack1 else 0
            val2= stack2.pop() if stack2 else 0
            total=val1+val2+carry
            carry=total//10
            
            new_node=ListNode(total%10)
            new_node.next=result
            result=new_node
        return result

if __name__=="__main__":
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    res=eraseOverlapIntervals(intervals)
    print(res)