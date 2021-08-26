# ---------------
# MAIN FILE
# ---------------

from sim_program_counter import ProgramCounter
from sim_memory import Memory
from sim_register_file import RegisterFile
from sim_execution_engine import ExecutionEngine
from sim_converter import *

def main():
    memory = Memory()
    registerFile = RegisterFile()
    executionEngine = ExecutionEngine(memory, registerFile)
    PC = ProgramCounter(0)

    halt = False
    cycle = 0

    while not halt:
        inst = memory.fetch(PC.getVal(), cycle)
        halt, nextPC = executionEngine.execute(inst, cycle)
        PC.dump()
        registerFile.dump()
        PC.update(nextPC)
        cycle += 1

    memory.dump()
    memory.showTraces()

if __name__ == '__main__':
    main()
