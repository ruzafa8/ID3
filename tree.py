class Tree:

    def __init__(self,attribute,leaf):
        self.isLeaf = leaf
        self.attribute = attribute
        self.values = []
        self.trees = []
    
    def addChildren(self, value, tree):
        self.values.append(value)
        self.trees.append(tree)

    def getChildren(self,value):
        i = 0
        while i < len(self.values) and value != self.values[i]:
            i = i + 1
        return None if i == len(self.values) else self.trees[i]