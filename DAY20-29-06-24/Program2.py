# Copy List with Random Pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldTocopy = { None : None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldTocopy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = oldTocopy[cur]
            copy.next = oldTocopy[cur.next]
            copy.random = oldTocopy[cur.random]
            cur = cur.next

        return oldTocopy[head]
