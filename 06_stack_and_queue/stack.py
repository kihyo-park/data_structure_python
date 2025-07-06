class Stack:
    def __init__(self, array_size : int, top : int, array : list):
        self.array_size = array_size
        self.top = top
        self.array = array
    def __str__(self):
        return f"Array: {self.array}, Top element: {self.top}, Array size: {self.array_size}"

def StackPush(Stack, value):
    if Stack.top == Stack.array_size - 1:
        Stack.array_size += 1    
    Stack.top += 1
    Stack.array[Stack.top] = value

s = Stack(4, 3, [0, 1, 2, 3])
print(s)