class LinkedListnode:
    def __init__(self, value = None):
        self.value = value
        self.next = None # The 'Pointer' or Reference that holds the location in memory of the next LinkedListnode object in the sequence.
    def __str__(self):
        if self.next is not None:
            next_val = self.next.value
        else:
            next_val = None
        # print the next node's value or just print 'None' if there's no value on the node.
        return f"Node(value: {self.value}, next: {next_val})" 

    def __repr__(self):
        
         return f"LinkedListnode({self.value})"
    
def LinkedListLookUp(LinkedListnode, element_number : int):
    current = LinkedListnode
    count: int = 0

    while count < element_number and current != None:
        current = current.next
        count = count + 1
    
    return current

head_node = LinkedListnode(10) # element 0
node2 = LinkedListnode(20) # element 1
node3 = LinkedListnode(30) # element 2
node4 = LinkedListnode(40) # element 3

# link the nodes together
head_node.next = node2
node2.next = node3
node3.next = node4
# This actually forms a linked list, Kihyo you stupid fuck.

print(head_node)
print(LinkedListLookUp(head_node, 3))