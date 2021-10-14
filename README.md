# Assembler and Simulator
Repository by Jaideep Guntupalli, Kabir Singh Mehrok and Jatin Tyagi.

This repository contains an Assembler and Simulator.

## Assembler
Assembler takes in assembly language as input and returns 16 bit machine code.

Each line of the input may be of one of 4 types: 
* Empty line: Ignore these lines 
* A label followed by an instruction 
* An instruction 
* A variable definition 

Each of these entities have the following grammar: 
* The syntax of all the supported instructions is given above. The fields of an instruction are whitespace separated. The instruction itself might also have whitespace before it. An instruction can be one of the following: 
	* The opcode must be one of the supported mnemonic. 
	* A register can be one of R0, R1, … R6, and FLAGS. 
	* A mem_addr in jump instructions must be a label. 
	* A Imm must be a whole number <= 255 and >= 0. 
	* A mem_addr in load and store must be a variable. 
* A label marks a location in the code and must be followed by a colon (:). No spaces are allowed between label name and colon(:). A label name consists of alphanumeric characters and underscores. 
A label followed by the instruction may looks like: 
					mylabel: add R1 R2 R3 
* A variable definition is of the following format: 
					var xyz 
which declares a 16 bit variable called xyz. This variable name can be used in place of mem_addr fields in load and store instructions. All variables must be defined at the very beginning of the assembly program. A variable name consists of alphanumeric characters and underscores. 
* Each line may be preceded by whitespace. 

### The assembler is be capable of: 
1. Handling all supported instructions 
2. Handling labels 
3. Handling variables 
4. Making sure that any illegal instruction (any instruction (or instruction usage) which is not supported) results in a syntax error. In particular you must handle: 
	a. Typos in instruction name or register name  
	b. Use of undefined variables  
	c. Use of undefined labels  
	d. Illegal use of FLAGS register  
	e. Illegal Immediate values (less than 0 or more than 255)  
	f. Misuse of labels as variables or vice-versa  
	g. Variables not declared at the beginning  
	h. Missing hlt instruction  
	i. hlt not being used as the last instruction  
	j. Wrong syntax used for instructions (For example, add instruction being used as a type B instruction )  
Distinct readable errors will be generated for all these conditions. The assembler will print out all these errors. 
If the code is error free, then the corresponding binary is generated. The binary is printed on to the console in which each line is a 16bit binary number written using 0s and 1s in ASCII. The assembler can write less than or equal to 256 lines. 

### Example of an assembly program 

Input:

var X  
mov R1 $10  
mov R2 $100  
mul R3 R1 R2  
st R3 X  
hlt  

The above program will be converted into the following machine code

0001000100001010  
0001001001100100  
0011000011001010  
0010101100000101  
1001100000000000  


The assembler code exists in the `Simple-Assembler` directory.

Run the shell script in `Simple-Assembler/run` in a bash terminal to execute the Assembler

## Simulator
Simulator takes in 16 bit machine code as input and prints/dumps memory state at the end of the program.

The simulator will load the binary in the system memory at the beginning, and then start executing the code at address 0. The code is executed until hlt is reached. After execution of each instruction, the simulator will output one line containing an 8-bit number denoting the program counter. This will be followed by 8 space-separated 16-bit binary numbers denoting the values of the registers (R0, R1, … R6, and FLAGS).

The input will be read from stdin.

Output format:
<PC (8 bits)> <space> <R0 (16 bits)> <space>...<R6 (16 bits)> <space> <FLAGS (16 bits)>

The output will be written to stdout.

After the program is halted, print the memory dump of the whole memory. This should be 256 lines, each having a 16-bit value 

< 16-bit data> 
< 16-bit data> 
….. 
< 16-bit data> 

The simulator also have the following distinct components: 
1. Memory (MEM): MEM takes in an 8-bit address and returns a 16-bit value as the data. The MEM stores 512bytes, initialized to 0s. 
2. Program Counter (PC): The PC is an 8-bit register that points to the current instruction. 
3. Register File (RF): The RF takes in the register name (R0, R1, … R6 or FLAGS) and returns the value stored at that register. 
4. Execution Engine (EE): The EE takes the address of the instruction from the PC, uses it to get the stored instruction from MEM, and executes the instruction by updating the RF and PC. 

The Simulator code exists in the `SimpleSimulator` directory.

Run the shell script in `SimpleSimulator/run` in a bash terminal to execute the Simulator.

	
## Additional Details about ISA, FLAGS semantics and more

* Details about the ISA, FLAGS semantics, Binary Encoding and Executable binary syntax is explanied in the below pdf.

[Assembler and Simulator.pdf](https://github.com/JaideepGuntupalli/CO_Assignment/files/7346495/Assembler.and.Simulator.pdf)

## Adding code
* Add the assembler code in the `Simple-Assembler` directory. Add the commands to execute the assembler in `Simple-Assembler/run`.
* Add the simulator code in the `SimpleSimulator` directory. Add the commands to execute the assembler in `SimpleSimulator/run`.
* Make sure that both the assembler and the simulator read from `stdin`.
* Make sure that both the assembler and the simulator write to `stdout`.

	
##How to evaluate the commits

* Go to the automatedTesting directory and execute the run file with appropiate options passed as arguments.
* Options available for automated testing:
        --verbose: Prints verbose output
        --no-asm: Does not evaluate the assembler
        --no-sim: Does not evaluate the simulator
