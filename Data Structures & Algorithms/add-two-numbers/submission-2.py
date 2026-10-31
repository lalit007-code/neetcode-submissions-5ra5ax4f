# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        currl1 = l1
        currl2 = l2
              
        dummy = ListNode()
        curr = dummy
        carry = 0

        while currl1 or currl2 or carry:
            val1 = currl1.val if currl1 else 0
            val2 = currl2.val if currl2 else 0
            
            total = val1 + val2 + carry
            newNode = total % 10
            carry = total//10
            print(total,newNode,carry)
            curr.next = ListNode(newNode)
            curr = curr.next
            currl1 = currl1.next if currl1 else None
            currl2 = currl2.next if currl2 else None
        
        return dummy.next