# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # finding half 
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        second = slow.next
        slow.next = prev = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        # now combining it with previous 
        # because previous has 2nd half head
        # print(prev.next.val)
        # dummy = ListNode()
        # second = head
        # d = dummy
        # while second:
        #     d.next = second
        #     d.next.next = prev
        #     second = second.next
        #     prev = prev.next
        #     d = d.next
        # return d.next


        first,second = head,prev

        while second:
            t1,t2 = first.next,second.next

            first.next,second.next = second,t1

            first,second = t1,t2
        