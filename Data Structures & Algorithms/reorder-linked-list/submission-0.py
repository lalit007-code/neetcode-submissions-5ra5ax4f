# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l1 = slow
        second = slow.next


        #breaking the  half
        prev = slow.next = None

        #     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev,curr = None, head

        # # 1 -> 2 -> 3
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # return prev

        while second:
            temp = second.next # saving pointer in temp variable
            second.next = prev # to previopud pointer for 0th it will be None for reverse purpose
            prev = second # saving curr pointer to link next pointer to it
            second = temp # incrementing the pointer
        

        # merge the two halfs
        # -> prev going to point to head 
        first, second = head,prev

        while second:
            temp1 ,temp2= first.next,second.next

            first.next, second.next = second, temp1
            
            # for moving forward using temp var
            ## i did mistake here used next, which will be initilaising the next pointer again
            first, second = temp1,temp2


            
        