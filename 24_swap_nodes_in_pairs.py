class LinkedNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def list_to_linked(list):
    head = LinkedNode(list[0], None)
    curnode = head
    for i in range(1, len(list)):
        curnode.next = LinkedNode(list[i], None)
        curnode = curnode.next
    return head


def linked_to_list(head):
    curnode = head
    list = []
    while curnode:
        list.append(curnode.val)
        curnode = curnode.next
    return list


def swapPairs(head):
    def helper(head):
        if head is None:
            return head
        if head.next is None:
            return head
        print(head.val, head.next.val)
        head.val, head.next.val = head.next.val, head.val
        head.next.next = helper(head.next.next)
        return head
        print(head.val, head.next.val)
    return helper(head)


print(linked_to_list(swapPairs(list_to_linked([1, 2, 3, 4]))))

