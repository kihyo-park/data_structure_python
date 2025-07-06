class Stack:
    def __init__(self, array_size : int, top : int, array : list):
        self.array = list(array)
        self.array_size = len(array)
        self.top = array[-1] # 이거 안 써도 되는 것 같은데 지우기...
    def __str__(self):
        return f"Array: {self.array}, Top element: {self.top}, Array size: {self.array_size}"

    def push(self, value):
        if self.top == self.array_size - 1:
            new_size = self.array_size * 2
            new_array = [None] * new_size 
        
            for i in range(self.array_size):
                new_array[i] = self.array[i]
        
            self.array = new_array
            self.array_size = new_size

        self.top += 1
        self.array[self.top] = value

s = Stack(4, 5, [0])
print(s)
#s.push(6)
#print(s)