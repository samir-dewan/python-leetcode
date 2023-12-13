# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #We have two arrays: [a, b, c] and [x, y, z].
        #when we call the function, we want to
        #join each array together
        #reverse each array
        #add one array to the second array
        #then the total array will be reversed again
        #then split back into an array
        #and then returned.
        #O(n + m)? Will depend on how long it takes joining and splitting an array

        #The better way of doing it would be:
        #output = []
        #Make lists same size
        #if l1.length < l2.length:
            #for i in l2.length - l1.length:
                #l1.append(0)
        
        #if l2.length < l1.length:
            #for i in l1.length - l2.length:
                #l2.append(0)
        #for each element i in arrays l1,l2:
        #result = l1[i] + l2[i] + ten-digit
        #ten-digit = 0
        #if result >= 10:
            #ten-digit = 1
            #result -= 10
        #output[i] = result

        output = ListNode()
        current_node = output
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            remainder = total % 10
        
            current_node.next = ListNode(remainder)
            current_node = current_node.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return output.next