class Table:

    def __init__(self, table):
        self.values = table

    def printTable(self, validRows, validCols):
        for i in range(0, len(self.values)):
            if validRows[i]:
                for j in range(0, len(self.values[i])):
                    if validCols[j]:
                        print(self.values[i][j], end=" ")
                print("")

    def getCol(self, x, validRows, validCols):
        res = []

        for i in range(0, len(self.values)):
            if validRows[i]:
                res.append(self.values[i][x])
        return res

    #def getRow(self, x):
    #    res = []
    #    for i in range(0, len(self.values[x])):
    #        res.append(self.values[x][i])
    #    return res

    def getDecisionCol(self, validRows, validCols):
        res = []

        for i in range(0, len(self.values)):
            if validRows[i]:
                res.append(self.values[i][-1])
        return res

    def getValue(self, x, y):
        return self.values[x][y]

