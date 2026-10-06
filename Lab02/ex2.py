import random

def bolnavi():

    bolnav = random.random()

    if bolnav <= 0.01:

        test = random.random()
        if test <= 0.95:
            return 'pozitiv'
        else:
            return 'fals negativ'
    else:
        test = random.random()
        if test <= 0.95:
            return 'fals pozitiv'
        else:
            return 'negativ'

rezultate = []
for i in range(1000):
    rezultate.append(bolnavi())
        
poz = [x for x in rezultate if x == 'pozitiv']

print(len(poz)/len(rezultate))