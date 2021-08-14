# THIS FILE INTENTION IS TO MAKE type_check() FN
# which will help us identify types of instructions

# We also added special notations to findout label and variable declaration
# and report these to the required place


'''
 Types : A, B, C, D, E, F
A TYPE : 4 ELEMENTS
B TYPE : 3 ELEMENTS AND LAST ELEMENT STARTS WITH $
C TYPE : 3 ELEMENTS AND BOTH REGISTERS
D TYPE : 3 ELEMENTS AND LAST ONE IS MEMORY ADDRESS
E TYPE : 2 ELEMENTS
F TYPE : 1 ELEMNTS,HALT(TO END)

Special notations :-
lbl TYPE : Preceeding any instruction with a label name and ":" at the end of name
var TYPE : 2 Elements with first being "var" and next being a variable name
'''


def type_check(command_individual_line):

    if command_individual_line[0][-1] == ":":
        result = 'lbl'

    else:

        if len(command_individual_line) == 4:
            result = 'A'

        elif len(command_individual_line) == 3:

            if command_individual_line[2][0] == '$':
                result = 'B'

            elif len(command_individual_line[0]) == 2:
                result = 'D'

            else:
                result = 'C'

        elif len(command_individual_line) == 2:

            if command_individual_line[0] == "var":
                result = 'var'

            else:
                result = 'E'

        elif len(command_individual_line) == 1:
            result = 'F'

    return result
