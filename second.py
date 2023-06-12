def addTwoNumbers( l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    dummy=ListNode(0)
    current=dummy
    carry=0
    while l1 or l2 or carry:
        sum1=carry
        if l1:
            sum1+=l1.val
            l1=l1.next
        if l2:
            sum1+=l2.val
            l2=l2.next
        carry=sum1//10
        current.next=ListNode(sum1%10)
        current=current.next
    return dummy.next

        

if __name__=="__main__":
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]
    addTwoNumbers(l1,l2)