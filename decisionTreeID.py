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

        self.i = 0
        self.tree = self.ID3(validRows, validCols)

    def ID3(self,validRows,validCols):
        self.i = self.i + 1
        print("iterations", self.i)
        print("validRows", validRows)
        print("validCols", validCols)
        print("Table", self.table.printTable(validRows, validCols))

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
                    print("G(Attr{}) = ".format(i), end="")
                    print(math.ganancia(self.table.getCol(i,validRows,validCols),targetAttribute))

                    # Take the attribute with the bigger ganance.
                    if g >= mayorGanancia:
                        mayorGanancia = g
                        attrMayorGanancia = i

            print("And the winner is: Attr",attrMayorGanancia, "->", mayorGanancia)
            tree = Tree(attrMayorGanancia,False)
            
            colMayorGanancia = self.table.getCol(attrMayorGanancia,validRows,validCols)

            # For each value of the attribute with the biggest ganance.
            for value in dict.fromkeys(colMayorGanancia):
                # Remove rows from the values of the attribute different for the selected one
                rowsToKeep = math.ocurrencias(colMayorGanancia,value)
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
            print("No hay más attributes: ", targetAttribute)
            # For each value of the target attribute see the one that is more frequent
            biggest = 0
            mostRepeatedValue = 0
            for value in dict.fromkeys(targetAttribute):
                ocurrence = targetAttribute.count(value)
                if biggest < ocurrence:
                    biggest = ocurrence
                    mostRepeatedValue = value
            print("AN DA WINER IS:", mostRepeatedValue)
            return Tree(mostRepeatedValue,True)
    
    def drawDecisionTree(self):
        DecisionTree.showWithLevel(self.tree, 0)
        # showWithLevel(self.tree, 0)

    def prediction(self, predicts):
        lector = csv.reader(predicts, delimiter=",")
        elementos = list(lector)[:-1]
        self.predict(elementos)

    def predict(self,elementos):
        if (self.tree.isLeaf):
            print(self.attribute)
        elif elementos == []:
            raise Exception()
        else:
            self.tree.getChildren(elementos[0]).predict(elementos[1:])       


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
#showWithLevel :: Tree -> Int -> [Char]
#showWithLevel (Leaf f) lvl =  "Output: " ++ show f
#showWithLevel (Node l r v) lvl = 
#    "Node x < " ++ show v ++ ":\n" ++ 
#    duplicate "\t" lvl ++ "- Left " ++
#    showWithLevel l (lvl+1) ++ "\n" ++ 
#    duplicate "\t" lvl ++ "- Right " ++ showWithLevel r (lvl+1)

