# ---------------
# MAIN FILE
# ---------------

from ProgramCounter import ProgramCounter
from Memory import Memory
from RegisterFile import RegisterFile
from ExecutionEngine import ExecutionEngine
from Converter import *

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
    # memory.showTraces()

if __name__ == '__main__':
    main()
