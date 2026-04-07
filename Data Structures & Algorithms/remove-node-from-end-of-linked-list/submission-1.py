# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two edge case
        # remove head and list hash only 1 element
        curr  = head
        if curr.next == None:
            head = None
            return
        
        count = 0
        while curr:
            count+=1
            curr = curr.next
        
        curr = head
        target = count - n
        # print("target",target)
        
        if target == 0:
            head = curr.next
            return head


        i = 0
        while i<target-1 and curr:
            i+=1
            curr = curr.next
        
        # print("curr.val",curr.val,'[i]',i)
        curr.next = curr.next.next
        return head
            
        