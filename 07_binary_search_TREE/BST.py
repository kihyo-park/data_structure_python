class Node:
    def _init__(self, key):
        # We represent trees in terms of linking nodes.
        self.key = key
        self.parent = self.left = self.right = None

    def __str__(self):
        return str(self.key)
 