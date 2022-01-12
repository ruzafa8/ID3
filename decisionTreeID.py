from table import Table
import mathematics as math
from tree import Tree
import numpy as np
import csv

class DecisionTree:

    def learnDT(self,csvFile):
        reader = csv.reader(open(csvFile,"rt"), delimiter=",")
        read = list(reader)
        self.table = Table(read)

        validRows = [True] * len(read)
        validCols = [True] * len(read[0])

        # table.printTable(validRows,validCols)
        # targetAttribute = table.getDecisionCol(validRows,validCols)

        # print("E(S) = ", math.entropia(targetAttribute))
        self.i = 0
        self.tree = self.ID3(validRows, validCols)

    def ID3(self,validRows,validCols):
        self.i = self.i + 1
        print("iii", self.i)
        targetAttribute = self.table.getDecisionCol(validRows,validCols)
        mayorGanancia = 0
        attrMayorGanancia = 0

        # For each attribute, calculate the ganance.
        for i in range(self.table.numAttributes(validRows,validCols) - 1): 
            g = math.ganancia(self.table.getCol(i,validRows,validCols),targetAttribute)
            print("G(Attr{}) = ".format(i), end="")
            print(math.ganancia(self.table.getCol(i,validRows,validCols),targetAttribute))

            # Take the attribute with the bigger ganance.
            if g > mayorGanancia:
                mayorGanancia = g
                attrMayorGanancia = i
        print("And the winner is:",attrMayorGanancia, "->", mayorGanancia)
        tree = Tree(attrMayorGanancia,False)
        
        colMayorGanancia = self.table.getCol(attrMayorGanancia,validRows,validCols)
        for value in dict.fromkeys(colMayorGanancia):
            # Remove rows from respectives values of the attribute
            rowsToDelete = math.ocurrencias(colMayorGanancia,value)
            cpyValidRows = validRows
            for idx in rowsToDelete:
                cpyValidRows[idx] = False
            
            # Remove column from attribute
            cpyValidCols = validCols
            cpyValidCols[attrMayorGanancia] = False

            # Recursive call
            if self.i < 5:
                tree.addChildren(value, self.ID3(cpyValidRows,cpyValidCols))
        return tree

    def drawDecisionTree():
        pass

    def prediction():
        pass