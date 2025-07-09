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
    
class Stack:
    def __init__(self):
        self.head = None

    def IsEmpty(self):
        if self.head == None:
            return True
        
    def Top(self):
        value = None
        if self.IsEmpty() == True:
            print("Stack is empty.")
        else:
            value = self.head.value
            return f"Current Linked List Stack's top element: {value}"

    def Push(self, value):
        new_node = LinkedListNode(value)
        new_node.next = self.head
        self.head = new_node
        print(self.head)

    def Pop(self):
        value = None
        if self.IsEmpty() == True:
            print("Stack is empty.")
        else:
            value = self.head.value # Set current head's value as None
            self.head = self.head.next # Set the value pointed by the current head as the current head's value.
            print(f"Pop {value}! Current Head Node: {self.head}")
    
s = Stack()
#print(s.Top())
s.Push(10)
s.Push(20)
s.Push(30)
s.Pop()
print(s.Top())
