class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None # Початкова висота нового вузла - 1

    def __str__(self, level=0, prefix="Root: "):
        ret = "\\t" * level + prefix + str(self.key) + "\\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret