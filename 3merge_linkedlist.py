class Node:
    def _init_(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_alternate(A, B):
    a = A
    b = B
    a_next = A.next

    while a and b:
        a.next = b
        b.next = a_next
        a = a_next
        b = b.next
        if a:
            a_next = a.next

    return A

A = Node(1, Node(2, Node(3)))


B = Node(4, Node(5, Node(6)))


A = merge_alternate(A, B)