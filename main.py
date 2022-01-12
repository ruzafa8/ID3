from decisionTreeID import DecisionTree as dt


tree = dt()
tree.learnDT("table.csv")
tree.drawDecisionTree()
tree.prediction()