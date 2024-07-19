class ListNode:
    def _init_(self, x):
        self.val = x
        self.next = None

def find_merge_node(head1, head2):
    nodes = set()
    while head1:
        nodes.add(head1)
        head1 = head1.next
    while head2:
        if head2 in nodes:
            return head2.val
        head2 = head2.next
    return -1

if _name_ == "_main_":
    # Setup linked lists for testing
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    
    head2 = ListNode(4)
    head2.next = head1.next
    
    print(find_merge_node(head1, head2))
