Question:
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

Example: Input: 1->2->3, Output: 1->2->4

            
            
1234 not_nine=4 1235
1249 not_nine=4 1250
1294 not_nine=4 1295
9999 not_nine=0 09999 19999 10000
    
    
    
    
    
    
    
    
Cand find a link video            

Solution:
    
    def plusOne(self, head:ListNode)->ListNode:
        dummy=ListNode(0)
        dummy.next=head
        not_nine=dummy
        
        while head:
            if head.val !=9:
                not_nine=head
            head=head.next
        
        not_nine.val+=1
        not_nine=not_nine.next
        
        while not_nine:
            not_nine.val=0
            not_nine=not_nine.next
            
        if dummy.val:
            return dummy
        else:
            return dummy.next
        

time O(n)
space O(1)
