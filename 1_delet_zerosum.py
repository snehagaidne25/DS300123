def delete_zero_sum(head):
    prefix_sum = 0
    sum_map = {}
    dummy = ListNode(0)
    dummy.next = head
    node = dummy

    while node:
        prefix_sum += node.val
        if prefix_sum in sum_map:
            prev_node = sum_map[prefix_sum].next
            current_sum = prefix_sum + prev_node.val
            while current_sum != prefix_sum:
                del sum_map[current_sum]
                prev_node = prev_node.next
                current_sum += prev_node.val
            sum_map[prefix_sum].next = node.next
        else:
            sum_map[prefix_sum] = node
        node = node.next

    return dummy.next