class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        if self.front is None:
            self.front = self.rear = Node(data)
        else:
            node = Node(data)
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            return None
        node = self.front
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        return node.data

    def is_empty(self):
        return self.front is None