# THIS FILE INTENTION IS TO MAKE A DOUBLE BYTE ADDRESSABLE MEMORY
# which for now will store instructions to convert them to machine code

def memory_adr(command_input):
    ''' Creates a memory with instructions by taking the whole error free instruction set
        Returns memory(with instructions which will be converted to memory code) and label_dict(which stores label names and memory address(in decimal))

        INPUT: 
            Instruction set
                The whole instructions set

        OUTPUT: 
            memory: With instructions which will be converted to memory code
            label_dict: Which stores label names and memory address(in decimal)

            Output will be a tuple of above
    '''

    memory = []  # Master memory which will be returned

    mem_var = []  # List to filter variables to store at the end

    label_dict = {}  # Dict to store labels

    line_cnt = 0  # Counter for storing label's declaration line

    for i in command_input:

        if i[0] != "var":  # If its not a variable declaration

            if i[0][-1] == ":":  # And a label, add it to a dict
                memory.append(i)
                label_dict[i[0][:-1]] = line_cnt

            else:
                memory.append(i)  # Else add to memory

            line_cnt += 1  # counting lines

        else:
            mem_var.append(i)  # variable memory storing

    memory += mem_var  # Adding variable after halt

    # Memory with corresponding instructions have been loaded

    # Labels are also extracted into a label_dict with key as label name and memory address as the value

    return memory, label_dict
