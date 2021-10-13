class Table:

    def __init__(self, table):
        self.values = table



    def printTable(self):
        for i in range(0, len(self.values)):
            for j in range(0, len(self.values[i])):
                print(self.values[i][j], end=" ")
            print("")

    def getCol(self, x):
        res = []
        for i in range(0, len(self.values)):
            res.append(self.values[i][x])
        return res

    def getRow(self, x):
        res = []
        for i in range(0, len(self.values[x])):
            res.append(self.values[x][i])
        return res

    def getValue(self, x, y):
        return self.values[x][y]

