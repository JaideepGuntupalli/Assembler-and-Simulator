# THIS IS FILE IS TO MAKE MACHINE CODE CONVERTERS FOR EACH TYPE OF INSTRUCTION

# ----- OP CODES and Reg Addresses -----

# Register addrs

reg = {"R0": "000",
       "R1": "001",
       "R2": "010",
       "R3": "011",
       "R4": "100",
       "R5": "101",
       "R6": "110",
       "FLAGS": "111"}


# OPCODES of Type A

opcodeA = {"add": "00000",
           "sub": "00001",
           "mul": "00110",
           "xor": "01010",
           "or": "01011",
           "and": "01100", }


# OPCODES of Type B

opcodeB = {"mov": "00010",
           "rs": "01000",
           "ls": "01001", }


# OPCODES of Type C

opcodeC = {"mov": "00011",
           "div": "00111",
           "not": "01101",
           "cmp": "01110", }


# OPCODES of Type D

opcodeD = {"ld": "00100",
           "st": "00101"}


# OPCODES of Type E

opcodeE = {"jmp": "01111",
           "jlt": "10000",
           "jgt": "10001",
           "je": "10010"}


# OPCODES of Type F

opcodeF = {"hlt": "10011"}


# ----- Decimal -> Binary [START]-----


def bin(dec_int):
    if dec_int == 0:
        return 0
    else:
        return (dec_int % 2 + 10 *
                bin(int(dec_int // 2)))


def dec_bin(dec_str):

    dec_int = int(dec_str)

    bin_int = bin(dec_int)

    bin_str = str(bin_int)

    return bin_str

# ----- Decimal -> Binary [END]-----


# ----- Binary Encoding -----
# These will convert the memory into machine code


# Binary Encoding of Type A

def binA(command_individual_line):
    '''
     opcode      unused       reg1        reg2        reg3
    (5 bits)    (2 bits)    (3 bits)    (3 bits)    (3 bits)
    '''

    # Getting the OPCODE
    machine_code = opcodeA[command_individual_line[0]]

    # Unused bits
    machine_code += "00"

    # Getting the register address
    for i in range(1, 4):
        machine_code += reg[command_individual_line[i]]

    return machine_code


# Binary Encoding of Type B

def binB(command_individual_line):
    '''
     opcode      reg1        $Imm
    (5 bits)    (3 bits)    (8 bits)
    '''

    # Getting the OPCODE
    machine_code = opcodeB[command_individual_line[0]]

    # Getting the register address
    machine_code += reg[command_individual_line[1]]

    # Convering immediate value to 8-bit binary
    imm = dec_bin(command_individual_line[2][1:])

    # Calculating total length to
    len_imm = len(imm)

    # Convert it to 8 bit memory address
    machine_code += (8-len_imm)*"0"

    # Adding it to machine code
    machine_code += imm

    return machine_code


# Binary Encoding of Type C

def binC(command_individual_line):
    '''
     opcode      unused       reg1        reg2
    (5 bits)    (5 bits)    (3 bits)    (3 bits)
    '''
    # Getting the OPCODE
    machine_code = opcodeC[command_individual_line[0]]

    # Unused bits
    machine_code += "00000"

    # Getting the register address
    for i in range(1, 3):
        machine_code += reg[command_individual_line[i]]

    return machine_code


# Binary Encoding of Type D

def binD(command_individual_line, memory, label_dict):
    '''
     opcode      reg1        Memory Address
    (5 bits)    (3 bits)    (8 bits)
    '''

    # Getting the OPCODE
    machine_code = opcodeD[command_individual_line[0]]

    # Getting the register address
    machine_code += reg[command_individual_line[1]]

    # From memory, insert the variable memory address

    for i in range(len(memory)):

        if memory[len(memory) - i - 1][-1] == command_individual_line[2]:
            mem_adr = dec_bin(len(memory) - i - 1)
            break

    # Calculating total length to
    len_mem_adr = len(mem_adr)

    # Convert it to 8 bit memory address
    machine_code += (8-len_mem_adr)*"0"

    # Adding it to machine code
    machine_code += mem_adr

    return machine_code


# Binary Encoding of Type E

def binE(command_individual_line, label_dict):
    '''
     opcode      unused     Memory Address
    (5 bits)    (3 bits)    (8 bits)
    '''

    # Getting the OPCODE
    machine_code = opcodeE[command_individual_line[0]]

    # Unused bits
    machine_code += "000"

    # From memory, insert the label memory address

    # Converting the decimal address to binary
    mem_adr = dec_bin(label_dict[command_individual_line[1]])

    # Calculating total length to
    len_mem_adr = len(mem_adr)

    # Convert it to 8 bit memory address
    machine_code += (8-len_mem_adr)*"0"

    # Adding it to machine code
    machine_code += mem_adr

    return machine_code


# Binary Encoding of Type F

def binF(command_individual_line):
    '''
     opcode      unused  
    (5 bits)    (11 bits)
    '''

    # Getting the OPCODE
    machine_code = opcodeF[command_individual_line[-1]]

    # Unused bits
    machine_code += "00000000000"

    return machine_code
