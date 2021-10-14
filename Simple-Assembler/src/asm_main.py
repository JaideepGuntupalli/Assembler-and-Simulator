# AUTHORS: Jaideep Guntupalli, Kabir Singh Mehrok and Jatin Tyagi

# This is the main file to run the whole assembler and output machine code from given instructions
# Also checking for any errors

# Files involved: asm_mem.py,asm_errors.py and asm-binary_encoder.py
# NOTES : Some files also require other files which are'nt mentioned here

import asm_binary_encoder as be
import asm_mem as mem
import asm_errors as ae
from sys import stdin


# Main

def main():

    # INPUT:

    command_input = []  # Empty list to add instructions
    total_commands = 0  # To count the total number of instructions

    for command_individual_line in stdin:

        if len(list(map(str, command_individual_line.split()))) != 0:  # Condition to ignore empty lines

            total_commands += 1  # Counting the number of instructions

            # If empty string(EOF) is read then stop the loop or if total instructions crossed 256
            if command_individual_line == '' or total_commands > 256:
                break

            # Converting the commands to list
            command_individual_list = list(
                map(str, command_individual_line.split()))

            # Appending to master list of commands
            command_input.append(command_individual_list)

    # Checking Any Errors in the given the instructions

    error_inspect = ae.error_check(command_input)

    if(error_inspect):
        return

    # Making memory of instructions and label dict
    memory, label_dict = mem.memory_adr(command_input)

    # Checking the command type and Computing machine code

    machine_code_list = be.pre_binary_encoder(
        command_input, memory, label_dict)

    # Printing the machine code
    for machine_code in machine_code_list:
        print(machine_code)


if __name__ == '__main__':
    main()
