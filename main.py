from table import Table
import mathematics as math

numAttributes = 2
#x = Table(askForTable(2))
x = Table([
    ["alta","alto","alto", "no", "no", "si"],
    ["alta","alto","alto", "si", "no", "si"],
    ["baja","alto","alto", "no", "no", "si"],
    ["media","alto","bajo", "no", "si", "no"],
    ["media","bajo","alto", "si", "si", "no"],
    ["baja","bajo","alto", "si", "si", "si"],
    ["alta","bajo","alto", "si", "no", "si"],
    ["alta","bajo","alto", "no", "si", "si"],
    ["alta","alto","bajo", "si", "si", "no"],
    ["baja","bajo","bajo", "si", "si", "si"],
    ["media","bajo","alto", "si", "si", "si"],
    ["alta","bajo","bajo", "si", "si", "no"],
    ["baja","alto","alto", "si", "si", "si"],
    ["baja","alto","bajo", "no", "no", "si"]
])
x.printTable()
targetAttribute = x.getCol(5)

print("Última columna: ", end="")
print(targetAttribute)

print("E(S) = ", end="")
print(math.entropia(targetAttribute))

print("G(F1) = ", end="")
print(math.entropiaRelativa(x.getCol(0),targetAttribute))



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


