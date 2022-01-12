from table import Table
import mathematics as math
from tree import Tree
import numpy as np
import csv

reader = csv.reader(open("table.csv","rt"), delimiter=",")
read = list(reader)

table = Table(read)

validRows = [True] * len(read)
validCols = [True] * len(read[0])

table.printTable(validRows,validCols)
targetAttribute = table.getDecisionCol(validRows,validCols)

print("Última columna: ", end="")
print(targetAttribute)

print("E(S) = ", end="")
print(math.entropia(targetAttribute))

#print("G(F1) = ", end="")
#print(math.ganancia(x.getCol(0,validRows,validCols),targetAttribute))
for i in range(6):
    print("G(Attr{}) = ".format(i), end="")
    print(math.ganancia(table.getCol(i,validRows,validCols),targetAttribute))

def ID3(validRows,validCols):
    targetAttribute = table.getDecisionCol(validRows,validCols)
    mayorGanancia = 0
    attrMayorGanancia = 0
    
    for i in range(6):
        g = math.ganancia(table.getCol(i,validRows,validCols),targetAttribute)
        if g > mayorGanancia:
            mayorGanancia = g
            attrMayorGanancia = i
    print(i)
    t = Tree(i,False)

def askForTable(attr):
    more = True
    values = []
    while more:
        row = []
        for i in range(0, attr):
            row.append(input())
        values.append(row)
        more = input("¿Desea añadir otra fila? (S/n)") == 'S'
    return values


