class Stack:
    def __init__(self, array_size : int, array : list):
        self.array = list(array)
        self.array_size = len(array)
        self.max_size = array_size
        self.top = self.array_size - 1 # 'top' is the INDEX of the top element
    def __str__(self):
        return f"Array: {self.array}, Top index: {self.top}, Array size: {self.array_size}"

    def IsEmpty(self):
        if self.array_size == 0:
            return True
            # or just return self.top == -1, where -1 means the top pointer is at the position indicating an empty stack (literally the index number '-1')
        
    def IsFull(self):
        if self.array_size == self.max_size:
            return True

    def Push(self, value):
        if self.IsFull() == True:
            print("Stack is full. Adding another empty slot...")
            old_size = self.max_size
        
            self.max_size = old_size + 1
        
            new_array = [None] * self.max_size

            self.array_size = len(new_array)

            for i in range(old_size):
                new_array[i] = self.array[i]
        
        self.array = new_array
        print(f"Added. New Max Size: {self.max_size}")

        self.top += 1
        self.array[self.top] = value

    def Pop(self):
        if self.IsEmpty() == True:
            print("Stack is empty.")
        else:
            del self.array[self.top]
            self.top -= 1
            print("Popped")


s = Stack(4, [0, 1, 2, 3])
print(s)
s.Push(6)
s.Pop()
print(s)
s.Pop()
print(s)
#s.push(6)
#print(s)