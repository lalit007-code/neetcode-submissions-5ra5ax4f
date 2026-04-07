# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:



        total = 0
        curr = head
        # remove head if head.next = None
        if curr.next == None:
            head = None
            return

        while curr:
            curr = curr.next
            total +=1

        idx = total - n
        i = 0
        curr = head

        if idx == 0:
            # removing head and making new head
            head = curr.next
            return head

        while i < idx-1 and curr:
            i += 1
            curr = curr.next
        print(total,idx,i)
        if curr and curr.next:
            curr.next = curr.next.next
        else:
            curr = curr.next
        return head
        