class Node:
    def _init_(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_in_groups(head, k):
    if not head or not head.next or k == 1:
        return head
    
    result = Node(0)
    result_tail = result
    stack = []
    
    while head:
        count = 0
        
    
        while head and count < k:
            stack.append(head)
            head = head.next
            count += 1
        

        if count == k:
            while stack:
                result_tail.next = stack.pop()
                result_tail = result_tail.next
        
        
        else:
            while stack:
                result_tail.next = stack.pop(0)
                result_tail = result_tail.next
    
    result_tail.next = None
    return result.next


head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))


head = reverse_in_groups(head, 3)
