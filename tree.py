class Tree:

    def __init__(self, attribute, isLeaf):
        self.isLeaf = isLeaf
        self.attribute = attribute # This variable represent the attribute name on a non-leaf node
                                   # and a the decision result on a leaf node.
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

    def predict(self,elementos):
        if (self.isLeaf):
            return self.attribute
        else:
            print("----------------------------")
            print(self.attribute)
            print(self.values)
            print(elementos)
            rama = elementos[self.attribute]
            print(rama)
            i = self.values.index(rama)
            return self.trees[i].predict(elementos)
