

def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    
    dummy=ListNode(-1)
    current=dummy
    while list1 and list2:
        if list1.val<list2.val:
            current.next=list1
            list1=list1.next
        else:
            current.next=list2
            list2=list2.next
        current=current.next
    current.next=list1 if list1 else list2
    return dummy.next
    
if __name__=="__main__":
    list1 = [1,2,4]
    list2 = [1,3,4]
    res=mergeTwoLists(list1,list2)
    print(res)