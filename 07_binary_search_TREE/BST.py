class Node:
    def __init__(self, key):
        # We represent trees in terms of linking nodes.
        self.key = key
        self.parent = self.left = self.right = None

    def preorder(self):
        if self != Node:
            print(self.key)
            
            if self.left:
                self.left.preorder()
                print(self.key)
            
            if self.left:
                self.right.preorder()
                print(self.key)

    def __str__(self):
        return str(self.key)
 
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

# draw the tree following these lines
a.left = b # 9
a.right = c
b.parent = c.parent = a
b.right = d
b = d.parent = e.parent



