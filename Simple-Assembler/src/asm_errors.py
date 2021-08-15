import string
'''ERRORS FILE'''

# All this list have been defined here
valid_var_char = list(string.ascii_lowercase +
                      string.ascii_uppercase + string.digits)
valid_var_char.append('_')
instruction_names_list = ["add", "sub", "mov", "ld", "st", "mul", "div",
                          "ls", "xor", "or", "and", "not", "cmp", "jmp", "jlt", "jgt", "je", "hlt"]
register_names_list = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"]
extended_register_names_list = ["R0", "R1",
                                "R2", "R3", "R4", "R5", "R6", "FLAGS"]
variable_names_list = []
label_names_list = []

def label_declaration(instruction_arr, label_names_list):
    ''' Checks whether the given label is declared properly 
        add the label to list of defined labels if it is declared properly        
    '''

    for i in range(len(instruction_arr)):
        if (instruction_arr[i][0][-1] == ":"):
            # label has been found
            if (len(instruction_arr[i]) == 1):
                # label is invalid
                continue
            else:
                # label is valid, store in list

                # Check whether label name is valid
                for j in instruction_arr[i][0][:-1]:
                    if(j in valid_var_char):
                        continue
                    else:
                        print(
                        f"LABEL_ERROR: In line {i+1} \n\tThe label name is invalid")
                        return True

                #Check whether its repeated or same as an instruction
                if ((instruction_arr[i][0][:-1] not in register_names_list) and (instruction_arr[i][0][:-1] not in instruction_names_list) and (instruction_arr[i][0][:-1] not in label_names_list)):
                    label_names_list.append(instruction_arr[i][0][:-1])
                else:
                    continue


def var_declare_check(command_individual_line, line):
    ''' Checks whether the given variable is declared properly 
        add the variable to list of defined variables if it is declared properly        
    '''
    # Checking whether instruction is 2 strings
    if(len(command_individual_line) == 2):
        # Checking whether the name is alphanumeric with underscores
        for i in command_individual_line[1]:
            if(i in valid_var_char):
                continue
            else:
                print(
                    f"VARIABLE_ERROR: In line {line} \n\tThe variable name is invalid")
                return True

        if(command_individual_line[1] not in variable_names_list):
            variable_names_list.append(command_individual_line[1])
            return False
        else:
            print(
                f"VARIABLE_ERROR: In line {line} \n\tThe variable has already been declared")
            return True

def errorA(command_individual_line,line):
    ''' Checks whether the given instruction for TYPE A is 
        declared properly and print errors if any present
    '''
    for i in range(1,4):
        if command_individual_line[i] in register_names_list:
            continue
        else:
            print(
            f"REGISTER_ERROR: In line {line} \n\tThe given register is invalid")
            return True

def errorB(command_individual_line,line):
    ''' Checks whether the given instruction for TYPE B is 
        declared properly and print errors if any present
    '''  
    if command_individual_line[1] in register_names_list:
        
        if command_individual_line[2][0] == "$":
        
            try:
                int(command_individual_line[2][1:])
                int_is = True
            except ValueError:
                int_is = False
                    
                if(int_is):
                    
                    if int(command_individual_line[2][1:]) >= 0 or int(command_individual_line[2][1:]) <= 255:
                        return False
                    
                    else:
                        print(
                        f"IMMEDIATE_ERROR: In line {line} \n\tThe given immediate value is illegal or not given properly")
                        return True
                
                else:
                    print(
                    f"IMMEDIATE_ERROR: In line {line} \n\tThe given immediate value is illegal or not given properly")
                    return True
    
    else:
        print(
        f"REGISTER_ERROR: In line {line} \n\tThe given register is invalid")
        return True

def errorC(command_individual_line,line):
    ''' Checks whether the given instruction for TYPE C is 
        declared properly and print errors if any present
    '''
    if command_individual_line[1] in register_names_list:

        if command_individual_line[2] in register_names_list:
            return False
        
        else:
            print(
                f"REGISTER_ERROR: In line {line} \n\tThe given register is invalid")
            return True
        
    else:
        print(
        f"REGISTER_ERROR: In line {line} \n\tThe given register is invalid")
        return True

def errorD(command_individual_line,line):
    ''' Checks whether the given instruction for TYPE D is 
        declared properly and print errors if any present
    '''
    if command_individual_line[1] in register_names_list:
        
        if command_individual_line[2] in variable_names_list:
            return False
        
        else:
            print(
                f"VARIABLE_ERROR: In line {line} \n\tUndefined variable has been used")
            return True
        
    else:
        print(
        f"REGISTER_ERROR: In line {line} \n\tThe given register is invalid")
        return True


def instruction_error_check(command_individual_line,line):
    ''' Checks whether the given instruction for  Different TYPES is 
        declared properly and print errors if any present
    '''

    # Len 4
    # TYPE A
    if(len(command_individual_line) == 4):

        typeA_valid_instructions = ["add","sub","mul","xor","or","and"]

        if command_individual_line[0] in typeA_valid_instructions:
            error = errorA(command_individual_line,line)

            if(error):
                return True
            else:
                return False
        
        else:
            print(
            f"SYNTAX_ERROR: In line {line} \n\tThe given instruction syntax is invalid")
            return True
    
    # Len 3
    elif(len(command_individual_line) == 3):

        typeC_valid_instructions = ["mov","div","not","cmp"]
        
        # mov (special case)
        if command_individual_line[0] == "mov":
        
            if command_individual_line[1] in register_names_list:
        
                if command_individual_line[2] in extended_register_names_list:
                    return False
        
                elif command_individual_line[2][0] == "$":
        
                    try:
                        int(command_individual_line[2][1:])
                        int_is = True
                    except ValueError:
                        int_is = False
                    
                    if(int_is):
                        
                        if int(command_individual_line[2][1:]) >= 0 or int(command_individual_line[2][1:]) <= 255:
                            return False
                        
                        else:
                            print(
                            f"IMMEDIATE_ERROR: In line {line} \n\tThe given immediate value is illegal or not given properly")
                            return True
                    
                    else:
                        print(
                        f"IMMEDIATE_ERROR: In line {line} \n\tThe given immediate value is illegal or not given properly")
                        return True
                
                else:
                    print(
                    f"REGISTER_ERROR: In line {line} \n\tThe given register is invalid")
                    return True
            
            else:
                print(
                f"REGISTER_ERROR: In line {line} \n\tThe given register is invalid")
                return True
        
        #TYPE B
        elif command_individual_line[0] == "rs" or command_individual_line[0] == "ls":

            if errorB(command_individual_line,line):
                return True
            
            else:
                return False
        
        #TYPE C
        elif command_individual_line[0] in typeC_valid_instructions:

            if errorC(command_individual_line,line):
                return True
            
            else:
                return False
        
        #TYPE D
        elif command_individual_line[0] == "ld" or command_individual_line[0] == "st":

            if errorD(command_individual_line,line):
                return True
            
            else:
                return False
        
        else:
            print(
            f"SYNTAX_ERROR: In line {line} \n\tThe given instruction syntax is invalid")
            return True
        
    # Len 2
    # TYPE E
    elif len(command_individual_line) == 2:

        typeE_valid_instructions = ["jmp","jlt","jgt","je"]

        if command_individual_line[0] in typeE_valid_instructions:

            if command_individual_line[1] in label_names_list:
                return False
            
            else:
                print(
                f"LABEL_ERROR: In line {line} \n\tThe given label is not declared")
                return True
        
        else:
            print(
            f"SYNTAX_ERROR: In line {line} \n\tThe given instruction syntax is invalid")
            return True
    
    #Len 1
    # TYPE F
    elif len(command_individual_line) == 1:

        if command_individual_line[0] == "hlt":
            print(
            f"HALT_ERROR: In line {line} \n\thlt not being used as the last instruction")
            return True
        
        else:
            print(
            f"SYNTAX_ERROR: In line {line} \n\tThe given instruction syntax is invalid")
            return True
    
    else:
        print(
        f"SYNTAX_ERROR: In line {line} \n\tThe given instruction syntax is invalid")
        return True


def error_check(command_input):

    # Valid Labels are being collected
    label_declaration(command_input, label_names_list)

    # This is too check whether we are at very beginning of the program
    var_declare = True

    label_names_list2=[]

    for i in range(len(command_input)):

        command_individual_line = command_input[i]

        if command_individual_line[0] == "var":

            # its variable declarations
            if(var_declare):

                if len(command_individual_line) == 2:
                    # Checking variable declaration
                    error = var_declare_check(command_individual_line, i+1)

                    if error:
                        return True
                
                else:
                    print(
                    f"VARIABLE_ERROR: In line {i+1} \n\tVariable declaration syntax is invalid")
                    return True

            else:
                print(
                    f"VARIABLE_ERROR: In line {i+1} \n\tAll variables must be defined at the very beginning")
                return True

        elif i < (len(command_input)-1):

            var_declare = False

            if command_individual_line[0] in instruction_names_list or command_individual_line[0][:-1] in label_names_list:
                
                # Its a valid first word
                if command_individual_line[0][:-1] in label_names_list:

                    if len(command_individual_line[0][:-1]) != 0:
                        continue
                    else:
                        print(
                            f"LABEL_ERROR: In line {i+1} \n\tThe declared label is empty")
                        return True

                    # This is to prevent double declaration of labels
                    if command_individual_line[0][:-1] not in label_names_list2:
                        label_names_list2.append(command_individual_line[0][:-1])
                    else:
                        print(
                            f"LABEL_ERROR: In line {i+1} \n\tThe given label has already been declared")
                        return True
            
                    # Its label Declaration
                    error = instruction_error_check(command_individual_line[1:],i+1)
                    if error:
                        return True
                else:
                    # Its a normal instruction
                    error = instruction_error_check(command_individual_line,i+1)
                    if error:
                        return True
            else:
                print(
                    f"INSTRUCTION_NAME_ERROR: In line {i+1} \n\tThe given instruction doesn't exist")
                return True
        
        else:

            if command_individual_line[0][:-1] in label_names_list:
            # Its a valid label
                if command_individual_line[1] == "hlt" and len(command_individual_line[0][:-1]) != 0:
                    return False
                else:
                    print(
                    f"SYNTAX_ERROR: In line {i+1} \n\tThe given instruction syntax is invalid")
                    print(
                    f"HALT_ERROR: In line {i+1} \n\tMissing or Invalid hlt instruction")
                    return True
                    
            else:
                if len(command_individual_line) == 1:
                    if command_individual_line[0] == "hlt":
                        return False
                    else:
                        print(
                        f"HALT_ERROR: In line {i+1} \n\tMissing or Invalid hlt instruction")
                        return True
                else:
                    print(
                        f"HALT_ERROR: In line {i+1} \n\tMissing or Invalid hlt instruction")
                    return True
