
import pyAgrum as gum
import pyAgrum.lib.notebook as gnb

model = gum.MarkovRandomField()

for node in ["A1", "A2", "A3", "A4", "A5"]:
    model.add(gum.LabelizedVariable(node, node, 2))

edges = [
    ("A1", "A2"),
    ("A1", "A3"),
    ("A2", "A4"),
    ("A2", "A5"),
    ("A3", "A4"),
    ("A4", "A5")
]

for a, b in edges:
    model.addArc(a, b)

gnb.show(model)