class LinkedListNode:
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
    
def LinkedListLookUp(LinkedListNode, element_number: int):
    current = LinkedListNode
    count: int = 0

    while count < element_number and current != None:
        current = current.next
        count = count + 1
    
    return current

def LinkedListInsert(node, index: int, value):
    '''
    node: The current node of the linked list
    index: The zero-based index for the new node.
    value: The value for the new node
    '''
    
    # create the new node to be inserted
    new_node = LinkedListNode(value)

    # insert the new head node at the begining of the linked list
    if index == 0:
        new_node.next = node
        return new_node
    
    # find the node at position (index - 1) to insert after it
    # why 'index - 1'? it's because you need to modify the next pointer of the node that comes !before! the insertion point
    # try just 'index' in the while loop and set your index as any number >= 1. You'll find something strange.
    # it's like you couple a new car X between Y and Z, you need to decopule Y and Z, couple Y to X, and couple X to Z. 
    current = node
    count: int = 0
    while count < index - 1 and current != None:
        current = current.next
        count += 1
    
    # check whether we reached at the end of the list before going into the inded that we need.
    if current == None:
        print(f"Index {index} is out of bounds!")
        return node
    
    # link the new node into the list
    new_node.next = current.next # find the node that current is pointing to, and make new_node point to it as well.
    current.next = new_node # 'rewiring'(=complete connecting new_node to somwhere in the middle of linked list when your defined index is >= 1)

    return node

def LinkedListDelete(node, index: int):

    if node == None:
        return None
    
    if index == 0:
        new_head = node.next
        return new_head

    current = node
    previous = None
    count: int = 0
    while count < index and current != None:
        previous = current
        current = current.next
        count += 1

    if current == None:
        print(f"Index {index} is out of bounds!")

    previous.next = current.next # Link the previous nod eto the node AFTER 'current'.

    return node

head_node = LinkedListNode(10) # element 0
node2 = LinkedListNode(20) # element 1
node3 = LinkedListNode(30) # element 2
node4 = LinkedListNode(40) # element 3

# link the nodes together
head_node.next = node2
node2.next = node3
node3.next = node4
# this actually forms a linked list: [10 -> 20 -> 30 -> 40 -> None]

# deleting node at index 0
test = LinkedListDelete(head_node, 0)
print(LinkedListLookUp(test, 0))

#new_node_inserted = LinkedListInsert(head_node, 0, 5) # index = 0
# now it shoud be [5 -> 10 -> 20 -> 30 -> 40 -> None] 
#print(LinkedListLookUp(new_node_inserted, 0))

#new_node_inserted = LinkedListInsert(head_node, 2, 5) # index = 2
# now it shoud be [10 -> 20 -> 5 -> 30 -> 40 -> None] 
#print(LinkedListLookUp(new_node_inserted, 2))
