# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        current1 = list1 
        current2 = list2

        

        if list1 == None:
            return list2
        if list2 == None: 
            return list1
        if list1.val <= list2.val:
            prev = list1
            current1 = current1.next
            head = list1 
        else:
            prev = list2
            current2 = current2.next
            head = list2

        while current1 != None and current2 != None: 
            
            if current1.val <= current2.val :
                prev.next = current1
                current1 = current1.next
            else:
                prev.next = current2
                current2 = current2.next
            prev = prev.next
            

        if current1 != None:
            prev.next = current1
        
        if current2 != None:
            prev.next = current2
    
        return head