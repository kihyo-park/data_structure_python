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
            
            if self.right:
                self.right.preorder()
                print(self.key)

    def inorder(self):
        if self.left:
            self.left.inorder()
        
        print(self.key)

        if self.right:
            self.right.inorder()
            print(self.key)

    def postorder(self):
        if self.left:
            self.left.postorder()
            print(self.key)

        if self.right:
            self.right.postorder()
        
        print(self.key)

    def __str__(self):
        return str(self.key)
 
root = Node("root")
a, b, c, d = Node("a"), Node("b"), Node("c"), Node("d")
e, f, g, h = Node("e"), Node("f"), Node("g"), Node("h")

b.parent = g.parent = root
root.left = b
root.right = f

a.parent = d.parent = a
b.left = a
b.right = d

c.parent = e.parent = d
d.left = c
d.right = e

g.parent = f
f.right = g

h.parent = g
g.left = h

root.postorder() # it shows the path of presenting nodes in preorder



