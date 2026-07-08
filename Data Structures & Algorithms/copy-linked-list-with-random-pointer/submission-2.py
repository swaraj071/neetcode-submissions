class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        oldToCopy = {None: None}

        curr = head

        while curr:
            # make copy of curr if not already made
            if curr not in oldToCopy:
                oldToCopy[curr] = Node(curr.val)

            copy = oldToCopy[curr]

            # make copy of curr.next if needed
            if curr.next not in oldToCopy:
                oldToCopy[curr.next] = Node(curr.next.val)

            # make copy of curr.random if needed
            if curr.random not in oldToCopy:
                oldToCopy[curr.random] = Node(curr.random.val)

            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]

            curr = curr.next

        return oldToCopy[head]