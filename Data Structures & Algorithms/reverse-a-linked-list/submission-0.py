# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while(head != None):
            stack.append(head)
            head = head.next

        if not stack:
            return None

        reveresedList = stack.pop()
        temp = reveresedList

        while (stack):
            node = stack.pop()
            temp.next = node
            temp = node
        
        temp.next = None
        return reveresedList