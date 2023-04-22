from collections import deque

def count_nodes_at_level(root, level):
    if not root:
        return 0
    queue = deque([(root, 0)])
    count = 0
    while queue:
        node, curr_level = queue.popleft()
        if curr_level == level:
            count += 1
        elif curr_level > level:
            break
        for child in node.children:
            queue.append((child, curr_level + 1))
    return count

class TreeNode:
    def _init_(self, val):
        self.val = val
        self.children = []

root = TreeNode(1)
root.children = [TreeNode(2), TreeNode(3)]
root.children[0].children = [TreeNode(4), TreeNode(5)]
root.children[1].children = [TreeNode(6), TreeNode(1)]

print(count_nodes_at_level(root, 2)) # Output: 3