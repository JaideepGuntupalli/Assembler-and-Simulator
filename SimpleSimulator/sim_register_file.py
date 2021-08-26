# ---------------
# REGISTER'S FILE
# ---------------

# Functions that are included in this file

# fetch(register_no)
#   fetches the value stored in a register
# update(register_no, value)
#   updates the value of the register to the given value
# dump()
#   prints values stored in all 7 registers

# FLAGS register operations 
# overflow()
# lessThan()
# greaterThan()
# equal()

from sim_converter import *

class RegisterFile:

    def __init__(self):
        register_stack = [
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000",
        "0000000000000000"
    ]
        self.register_stack = register_stack

    def fetch(self, register_no):
        '''
        Fetches the value stored in the register with given register number
        INPUT: 
            register_no: in binary
        OUTPUT: 
            returns register value: in binary
        '''

        index = bintodec(register_no)
        return self.register_stack[index]

    def update(self, register_no, value):
        '''
        Fetches the value stored in the register with given register number
        INPUT: 
            register_no: in binary
            value: 16 bit value in binary
        OUTPUT: 
            returns nothing
        '''
        index = bintodec(register_no)
        self.register_stack[index] = value
    
    def reset(self, register_no):
        '''
        resets a register to its 0 state
        INPUT: 
            register_no: in binary
        OUTPUT: 
            returns nothing
        '''
        index = int(register_no, 2)
        self.register_stack[index] = "0000000000000000"

    def dump(self):
        '''
        prints the values of all the 7 the register
        INPUT: 
            nothing
        OUTPUT: 
            returns nothing
            prints ><R0 (16 bits)><space>...<R6 (16 bits)><space><FLAGS (16 bits)>
        '''
        print(' '.join(map(str, self.register_stack)), end=' \n')
        return
        for index in range(len(self.register_stack)):
            print(self.register_stack[index], end =" ")
        print()

    # for the following methods keep in mind the syntax of FLAGS register

    # _ _ _ _ _ _ _ _ _ _ _  __ __ __ __ __
    # 0 0 0 0 0 0 0 0 0 0 0  0  V  L  G  E
    # _ _ _ _ _ _ _ _ _ _ _  __ __ __ __ __
    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

    def overflow(self):
        '''
        sets the overflow bit FLAGS register
        INPUT: 
            nothing
        OUTPUT: 
            returns nothing
        '''
        flagsList = list(self.register_stack[-1])
        flagsList[12] = "1"
        flags = "".join(flagsList)
        self.register_stack[-1] = flags
    
    def lessThan(self):
        '''
        sets the less than bit FLAGS register
        INPUT: 
            nothing
        OUTPUT: 
            returns nothing
        '''
        flagsList = list(self.register_stack[-1])
        flagsList[13] = "1"
        flags = "".join(flagsList)
        self.register_stack[-1] = flags
    
    def greaterThan(self):
        '''
        sets the greater than bit FLAGS register
        INPUT: 
            nothing
        OUTPUT: 
            returns nothing
        '''
        flagsList = list(self.register_stack[-1])
        flagsList[14] = "1"
        flags = "".join(flagsList)
        self.register_stack[-1] = flags

    def equal(self):
        '''
        sets the equality bit FLAGS register
        INPUT: 
            nothing
        OUTPUT: 
            returns nothing
        '''
        flagsList = list(self.register_stack[-1])
        flagsList[15] = "1"
        flags = "".join(flagsList)
        self.register_stack[-1] = flags


    # for the following methods keep in mind the syntax of FLAGS register

    # _ _ _ _ _ _ _ _ _ _ _  __ __ __ __ __
    # 0 0 0 0 0 0 0 0 0 0 0  0  V  L  G  E
    # _ _ _ _ _ _ _ _ _ _ _  __ __ __ __ __
    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

    def check_overflow(self):
        '''
        check the overflow bit FLAGS register
        INPUT: 
            nothing
        OUTPUT: 
            returns boolean value
        '''
        flagsList = list(self.register_stack[-1])
        
        return flagsList[12] == "1"
        
    
    def check_lessThan(self):
        '''
        check the less than bit FLAGS register
        INPUT: 
            nothing
        OUTPUT: 
            returns boolean value
        '''
        flagsList = list(self.register_stack[-1])

        return flagsList[13] == "1"
        
    
    def check_greaterThan(self):
        '''
        check the greater than bit FLAGS register
        INPUT: 
            nothing
        OUTPUT: 
            returns boolean value
        '''
        flagsList = list(self.register_stack[-1])

        return flagsList[14] == "1"

    def check_equal(self):
        '''
        check the equality bit FLAGS register
        INPUT: 
            nothing
        OUTPUT: 
            returns boolean value
        '''
        flagsList = list(self.register_stack[-1])
        
        return flagsList[15] == "1"