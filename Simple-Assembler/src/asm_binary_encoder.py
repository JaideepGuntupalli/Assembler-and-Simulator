# THIS IS A DRIVER CODE WHICH RUNS USING asm-opcode.py FUNCTIONS
# Files involved: asm_type_identifier and asm_opcode

import asm_type_identifier as ti
import asm_opcode as op

# ----- Driver Code -----
# Its using the functions from asm-opcode.py to make machine code for simulator


def binary_encoder(type, command_individual_line, memory, label_dict):

    if(type == "A"):
        machine_code = op.binA(command_individual_line)

    elif(type == "B"):
        machine_code = op.binB(command_individual_line)

    elif(type == "C"):
        machine_code = op.binC(command_individual_line)

    elif(type == "D"):
        machine_code = op.binD(command_individual_line, memory, label_dict)

    elif(type == "E"):
        machine_code = op.binE(command_individual_line, label_dict)

    elif(type == "F"):
        machine_code = op.binF(command_individual_line)

    elif(type == "lbl"):
        machine_code = binary_encoder(ti.type_check(
            command_individual_line[1:]), command_individual_line[1:], memory, label_dict)

    elif(type == "var"):
        machine_code = "ignore"

    return machine_code


# ----- Pre Driver Code -----
# This will take input from main function
# This is too keep main clean and clear

def pre_binary_encoder(command_input, memory, label_dict):

    machine_code_list = []  # Machine code list which will be made from memory

    for command_individual_line in command_input:

        # Checking type of individual instruction
        type = ti.type_check(command_individual_line)

        machine_code = binary_encoder(
            type, command_individual_line, memory, label_dict)  # Converting to machine code

        if(machine_code != "ignore"):  # After ignoring variables the machine code will be appended to list
            machine_code_list.append(machine_code)

    return machine_code_list
