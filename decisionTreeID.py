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

        numRows = len(read)
        self.numCols = len(read[0])

        validRows = [True] * numRows
        validCols = [True] * self.numCols

        self.tree = self.ID3(validRows, validCols)

    def ID3(self,validRows,validCols):

        targetAttribute = self.table.getDecisionCol(validRows,validCols)

        if(all(element == targetAttribute[0] for element in targetAttribute)):
            return Tree(targetAttribute[0],True)
        elif any(validCols[:-1]):
            mayorGanancia = 0
            attrMayorGanancia = 0
            
            # For each attribute, calculate the ganance.            
            for i in range(self.numCols - 1): 
                if validCols[i]:
                    g = math.ganancia(self.table.getCol(i,validRows,validCols),targetAttribute)

                    # Take the attribute with the bigger ganance.
                    if g >= mayorGanancia:
                        mayorGanancia = g
                        attrMayorGanancia = i

            tree = Tree(attrMayorGanancia,False)
            
            colMayorGanancia = self.table.getCol(attrMayorGanancia,validRows,validCols)
            colMayorGananciaAbs = self.table.getColTotal(attrMayorGanancia)

            # For each value of the attribute with the biggest ganance.
            for value in dict.fromkeys(colMayorGanancia):
                # Remove rows from the values of the attribute different for the selected one
                rowsToKeep = math.ocurrencias(colMayorGananciaAbs,value)
                cpyValidRows = validRows[:]
                for i in range(len(cpyValidRows)):
                    if not i in rowsToKeep:
                        cpyValidRows[i] = False
                
                # Remove column from attribute
                cpyValidCols = validCols[:]
                cpyValidCols[attrMayorGanancia] = False

                # Recursive call
                tree.addChildren(value, self.ID3(cpyValidRows,cpyValidCols))
            return tree
        else:
            # For each value of the target attribute see the one that is more frequent
            biggest = 0
            mostRepeatedValue = 0
            for value in dict.fromkeys(targetAttribute):
                ocurrence = targetAttribute.count(value)
                if biggest < ocurrence:
                    biggest = ocurrence
                    mostRepeatedValue = value

            return Tree(mostRepeatedValue,True)
    
    def drawDecisionTree(self):
        DecisionTree.showWithLevel(self.tree, 0)
        # showWithLevel(self.tree, 0)

    def prediction(self, predicts):
        lines = csv.reader(predicts)
        res = []
        for line in lines:
            x = csv.reader(line)
            l = list(x)
            predict = []
            for x in l:
                predict.append(x[0])

            res.append(self.tree.predict(predict))
        return res

    @classmethod
    def showWithLevel(self,arbol, level):
        if arbol.isLeaf:
            for i in range(level):
                print("\t", end="")
            print("Output: " + str(arbol.attribute))
        else:
            for value in arbol.values:
                for i in range(level):
                    print("\t", end="")
                print("Attribute"+str(arbol.attribute), end=": ")
                print(value)
                DecisionTree.showWithLevel(arbol.getChildren(value),level+1)

