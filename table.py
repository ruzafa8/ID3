class Table:

    def __init__(self, table):
        self.values = table

    def printTable(self, validRows, validCols):
        for i in range(0, len(self.values)):
            for j in range(0, len(self.values[i])):
                print(self.values[i][j], end=" ")
            print("")

    def getCol(self, x, validRows, validCols):
        res = []
        numOnes = 0
        idx = 0
        while idx < len(self.values) and numOnes == x:
            if validCols[idx]:
                numOnes = numOnes + 1
            idx = idx + 1
        if idx == len(self.values):
            raise IndexError()
        print("indice:", idx)
        for i in range(0, len(self.values)):
            if validRows[i]:
                res.append(self.values[i][idx])
        return res

    #def getRow(self, x):
    #    res = []
    #    for i in range(0, len(self.values[x])):
    #        res.append(self.values[x][i])
    #    return res

    def getDecisionCol(self, validRows, validCols):
        res = []
        pos = 0
        idx = -1

        for i in range(0, len(self.values)):
            if validRows[i]:
                res.append(self.values[i][idx])
        return res

    def getValue(self, x, y):
        return self.values[x][y]

