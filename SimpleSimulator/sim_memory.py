# ---------------
# MEMORY
# ---------------

# Functions that are included in this file

# fetch 
#   fetches the instruction corresponding to the given memory address
# dump
#   prints all the instructions in the memory
# showTraces
#   creates a scatter plot 

# Some variable that we need to make
# cycle_address
#   stores the address corresponding to the cycle in which that address was called

import matplotlib.pyplot as plt
from sys import stdin
from sim_converter import *

x_axis = []
y_axis = []

class Memory:
    #cycle = 0
    #cycle_address = []
    #memory_stack = []

    def __init__(self):
        # intiazlizes the memory by taking input
        self.cycle = 0
        self.cycle_address = []
        self.memory_stack = []
        self.memory_input()
        self.memory_creator()

    def getData(self, address):
        x_axis.append(self.cycle)
        y_axis.append(address)
        return self.memory_stack[address]

    def setData(self, address, data):
        x_axis.append(self.cycle)
        y_axis.append(address)
        self.memory_stack[address] = data

    def memory_creator(self):
        for i in range(256-len(self.memory_stack)):
            self.memory_stack.append("0000000000000000")
  
    def memory_input(self):
        for memory_instruction in stdin:
            if memory_instruction == '':
                break
            self.memory_stack.append(str(memory_instruction))

    def fetch(self, pc_val, cycle):
        # fetches the instruction corresponding to the given pc_val and returns it
        
        # at first we are updating the cycle and cycle_address
        #  which will be used for scatter plot
        self.cycle = cycle
        self.cycle_address.append(bintodec(pc_val))
        x_axis.append(cycle)
        y_axis.append(bintodec(pc_val))

        # now we return the address
        instruction_id = bintodec(pc_val)
        return self.memory_stack[instruction_id]


    def dump(self):
        # dumps all the memory instructions

        for i in range(len(self.memory_stack)):
            print(self.memory_stack[i].strip('\n'))


# This is part of question 3
    def showTraces(self):
        # generate a scatter plot with the cycle number on the x-axis 
        # and the memory address on the y-axis
        #cycle_number = [i for i in range(self.cycle+1)]
        
        # now we plot the graph

        #plt.scatter(cycle_number, self.cycle_address)


        plt.scatter(x_axis, y_axis)
        plt.xlabel("Cycle")
        plt.ylabel("Memory Address")
        plt.savefig('plot.png')
        return