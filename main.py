from decisionTreeID import DecisionTree as dt

tree = dt()
tree.learnDT("datos.csv")
tree.drawDecisionTree()
pred = tree.prediction(['bajo,rubio,marrones',
                        'alto,moreno,marrones',
                        'alto,rubio,azules',
                        'alto,moreno,azules',
                        'bajo,moreno,azules',
                        'alto,rojo,azules',
                        'alto,rubio,marrones',
                        'bajo,rubio,azules',
                        'bajo,moreno,marrones'])
print(pred)