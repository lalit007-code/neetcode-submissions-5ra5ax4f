# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #first we will find mid using slow and fast pointer
        # then will reverse the second half 
        # then while mergin both we will take a element from first half and another from second and if left any element
        # in any half we will give that address
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # now reverse the second one

        #note : if i have to reverse second then i have to start from second 
        prev ,curr = None, slow.next
        slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # reinitlaize the first
        first = head

        #second previous ke equals isiliye hoga kioki, prev last element pe hoga jo ki head hau
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        
        # while first:
        #     second.next = first
        
        # while second:
        #     first.next = second

        

