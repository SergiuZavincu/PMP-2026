import numpy as np

def simulare_extragere():
    
    urna = [1,2,3,4,5,6,7,8,9]

    zar = np.random.randint(1,6 +1)




def calc_prob(bila):
   
    red = 3
    blue = 4
    black = 2

    zar = np.random.randint(1,6 +1)

    if zar == 6:
        red +=1
    elif zar == 2 or zar == 3 or zar == 5:
        black +=1
    else:
        blue +=1

    
    if bila == "red":
        return red/(red+blue+black)
    elif bila == "blue":
        return blue/(red+blue+black)
    else:
        return black/(red+blue+black)
    
print(calc_prob("red"))



    