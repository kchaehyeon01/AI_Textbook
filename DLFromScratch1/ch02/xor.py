import numpy as np
from and_with_wb import AND
from nand_with_wb import NAND
from or_with_wb import OR

def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y

x1 = float(input("x1 : "))
x2 = float(input("x2 : "))
print(XOR(x1,x2))