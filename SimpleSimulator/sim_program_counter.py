# ---------------
# PROGRAM COUNTER
# ---------------

# Functions that are included in this file

# getVal
#   returns the value of PC
# update
#   updates the value of PC
# dump
#   prints the value of PC

# Some variable that we need to make
# PC
#   stores the address corresponding to the cycle in which that address was called

from sim_converter import *

class ProgramCounter:
    PC = "" # the value stored here is in binary

    def __init__(self, val):
        self.PC = format(val, "08b")

    def getVal(self):
        return self.PC
    
    def update(self, val):
        self.PC = val

    def dump(self):
        print(self.PC, end=" ")

