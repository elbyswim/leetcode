class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        if self.next is None:
            return str(self.data)
        else:
            return ', '.join([str(self.data), self.next.__str__()])


tests = [Node(1, Node(2, Node(3, Node(4)))),
         Node(1, Node(1, Node(3, Node(4)))),
         Node(1, Node(2, Node(1, Node(4)))),
         Node(1, Node(2, Node(3, Node(1))))]
for i, test in enumerate(tests):
    print('test {}:'.format(i), test)


# 2.1
def remove_dup(head):
    llist = Node(next=head)
    curr = llist
    seen = set()
    while curr.next is not None:
        seen.add(curr.data)
        if curr.next.data in seen:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return llist.next


for i, test in enumerate(tests):
    print('test {}:'.format(i), remove_dup(test))