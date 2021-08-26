from sim_converter import *

class ExecutionEngine:

    def __init__(self, memory, registerFile):
        to_return = [False, "00000000"]
        self.m = memory
        self.r = registerFile
        self.to_return = to_return

    def execute(self, inst, cycle):
        '''
        TYPE A:
        add:00000
        sub:00001
        mul:00110
        xor:01010
        or:01011
        and:01100

        TYPE B:
        mov(move immediate):00010
        rs:01000
        ls:01001

        TYPE C:
        mov(move register):00011
        div:00111
        not:01101
        cmp:01110

        TYPE D:
        ld:00100
        st:00101

        TYPE E:
        jmp(unconditional jump):01111
        jlt(jump if less than):10000
        jgt:10001
        je:10010

        TYPE F:
        hlt:10011

        TYPE A:
        5-BIT OP|2-BIT UNUSED|3BIT REG1|REG2|REG3
        TYPE B:
        5-BIT OP|3-BIT REG1|8BIT IMMEDIATE
        TYPE C:
        5-BIT OP|5-BIT UNUSED|3-BIT REG1|REG2
        TYPE D:
        5-BIT OP|3-BIT REG1|8-BIT MEMORY ADDRESS
        TYPE E:
        5-BIT OP|3_UNUSED|8-BIT MEMORY ADDRESS
        TYPE F:
        5-BIT OP|11-BIT UNUSED
        '''
        #making the lists of the op codes and defining the types of function

        a = ["00000","00001","00110","01010","01011","01100"]
        b = ["00010","01000","01001"]
        c = ["00011","00111","01110", "01101"]
        d = ["00100","00101"]
        e = ["01111","10000","10001","10010"]
        f = ["10011"]      
        
        # defining the function A
        def A(inst):
            
            self.r.reset("111")

            if inst[0:5]=="00000":
                
                #ADDITION
                b=(self.r.fetch(inst[10:13])) # 1st value for addition
                c=(self.r.fetch(inst[13:16])) # 2nd value for addition
                
                # Initialize the result
                answer = ''
                
                # Initialize the carry
                carry = 0
                
                # Traverse the string,this is the main part which performs addition
                for i in range(len(b) - 1, -1, -1):
                    z = carry
                    z += 1 if c[i] == '1' else 0
                    z += 1 if b[i] == '1' else 0
                    answer = ('1' if z % 2 == 1 else '0') + answer
                
                    # Compute the carry,this is to check for overflow
                    carry = 0 if z < 2 else 1
                
                if carry != 0: # calling overflow
                    self.r.overflow()
                
                self.r.update(inst[7:10],answer) # updating the value of the register



            elif inst[0:5]=="00001":
                
                #SUBTRACT
                a=(self.r.fetch(inst[10:13])) # 1st value for subtraction
                b=(self.r.fetch(inst[13:16])) # 2nd value for subtraction

                a = bintodec(a)
                b = bintodec(b)

                result = a-b
                if result < 0:
                    self.r.overflow()
                    result = 0

                self.r.update(inst[7:10], dectobin(result))
                '''                
                answer  = '' # for calculating answer
                carry   = 0  # variable which will check for overflow

                i = len(a) - 1
                
                while(i >= 0):
                    s = int(a[i]) - int(b[i])
                
                    if s <= 0: # loop for caluclating subtraction
                
                        if carry == 0 and s != 0:
                            carry = 1
                            answer = answer + "1"
                
                        else:
                            answer = answer + "0"
                
                    else:
                
                        if carry == 1:
                            answer = answer + "0"
                            carry = 0   
                
                        else:
                            answer = answer + "1" 
                
                    i = i - 1


                if carry>0: # if carry is there then assigning 0 to register and setting overflow
                    self.r.overflow()
                    self.r.update(inst[7:10],"0"*16)
                
                else: # else assigning value to register
                    answer=answer[::-1]
                    self.r.update(inst[7:10],answer)
                '''

            elif inst[0:5]=="00110":
                
                #MULTIPLY
                b=bintodec(self.r.fetch(inst[10:13])) # 1st value
                c=bintodec(self.r.fetch(inst[13:16])) # 2nd value
                mult=b*c
                
                if mult>65535:
                    self.r.overflow()
                    mult %= 65536
                    #mult=dectobin(mult)
                    # mult=mult-65535
                    #mult = mult[-16:]
                
                mult=dectobin(mult)
                #mult=mult.zfill(16)
                self.r.update(inst[7:10],mult)
                

            elif inst[0:5]=="01010":
                
                #XOR
                b=self.r.fetch(inst[10:13]) # 1st value
                c=self.r.fetch(inst[13:16]) # 2nd value
                
                final=""
                
                for i in range(len(b)): # performing the xor operation
                
                    if(b[i]==c[i]):
                        final=final+"0"
                
                    else:
                        final=final+"1"
                
                # updating the values
                self.r.update(inst[7:10],final)

            elif inst[0:5]=="01011":
                
                #OR
                b=self.r.fetch(inst[10:13]) # 1st value
                c=self.r.fetch(inst[13:16]) # 2nd value
                
                final=""
                
                final = dectobin(bintodec(b) | bintodec(c))
                
                # updating the values
                self.r.update(inst[7:10],final)

            elif inst[0:5]=="01100":
                
                #AND
                b=self.r.fetch(inst[10:13]) # 1st value
                c=self.r.fetch(inst[13:16]) # 2nd value
                
                final=""
                
                for i in range(len(b)):# performing the and operation
                
                    if((b[i]=="1") and (c[i]=="1")):
                        final=final+"1"
                
                    else:
                        final=final+"0"
                
                # updating the values
                self.r.update(inst[7:10],final)
                

        # Defining function for B
        def B(inst):
            self.r.reset("111")
            
            if inst[0:5]=="00010":
                #move immediate
                val = "0"*8 + inst[8:16]
                self.r.update(inst[5:8], val) # updating the value of register by the immediate value given

            elif inst[0:5]=="01000":
                #right shift
                a=self.r.fetch(inst[5:8])
                a=a[::-1]
                b=bintodec(inst[8:16])
                
                for i in range(b):
                    a=a+"0"
                
                a=a[::-1]
                final=a[0:-(b)]
                self.r.update(inst[5:8],final)


            elif inst[0:5]=="01001":
                #left shift
                a=self.r.fetch(inst[5:8])
                b=bintodec(inst[8:16])
                
                for i in range(b):
                    a=a+"0"
                
                final=a[b::1]
                self.r.update(inst[5:8],final)

        

        #defining for type C
        def C(inst):
            if inst[0:5]=="00011":
                #move register
                #getting the value stored in the 2nd register then updating the value of 1st register by the value of second register
                b=self.r.fetch(inst[13:16])
                self.r.update(inst[10:13],b)
                self.r.reset("111")

            elif inst[0:5]=="00111":
                #divide
                a=bintodec(self.r.fetch(inst[10:13]))#value of 1st register
                b=bintodec(self.r.fetch(inst[13:16]))#value of 2nd register
                c=dectobin(a//b) #quotient
                d=dectobin(a%b)#remainder
                #updating the values R0=QUOTIENT  R1=REMAINDER
                self.r.update("000",c)
                self.r.update("001",d) 
                self.r.reset("111")

            elif inst[0:5]=="01101":
                #not
                b=self.r.fetch(inst[13:16])#getting the value stored in the 2nd register
                final=~bintodec(b)&65535
                final=dectobin(final)
                self.r.update(inst[10:13],final)#updating value in 1st register as the inverted value of value in 2nd register
                self.r.reset("111")


            elif inst[0:5]=="01110":
                #compare
                #fetching values of registers
                a=self.r.fetch(inst[10:13])#value of 1st register
                b=self.r.fetch(inst[13:16])#value of 2nd register
                self.r.reset("111")
                if (a==b):
                    self.r.equal()
                elif (a>b):
                    self.r.greaterThan()
                elif (a<b):
                    self.r.lessThan()
            
            


        #defining for type D
        def D(inst):
            self.r.reset("111")
            if inst[0:5]=="00100":
                # load
                data = self.m.getData(bintodec(inst[8:16]))
                self.r.update(inst[5:8], data)

            elif inst[0:5]=="00101":
                # store
                data = self.r.fetch(inst[5:8])
                self.m.setData(dec(inst[8:16]), data)

        #defining for type E
        def E(self,inst):
            if inst[0:5]=="01111":
                #unconditional jump
                self.to_return[1] = inst[8:16]
                return True
            

            elif inst[0:5]=="10000":
                #jump if less than
                if (self.r.check_lessThan()):
                    self.to_return[1] = inst[8:16]
                    return True
                return False                    
                

            elif inst[0:5]=="10001":
                #jump if greater than
                if (self.r.check_greaterThan()):
                    self.to_return[1] = inst[8:16]
                    return True
                return False 

            elif inst[0:5]=="10010":
                #jump if equal
                if (self.r.check_equal()):
                    self.to_return[1] = inst[8:16]
                    return True
                return False 
        
        
        # CALLING THE FUNCTIONS BASED ON OPCODES
        
        if inst[0:5] in a:
            A(inst)
        
        elif inst[0:5] in b:
            B(inst)
        
        elif inst[0:5] in c:
            C(inst)
        
        elif inst[0:5] in d:
            D(inst)
        
        elif inst[0:5] in e:
        
            if (E(self,inst)):
                self.r.reset("111")
                return self.to_return
        
            self.r.reset("111")
        
        elif inst[0:5] in f:
        
            # we set halt to true
            self.r.reset("111")
            self.to_return[0] = True
            return self.to_return

        currPC = bintodec(self.to_return[1])
        nextPC = currPC + 1
        self.to_return[1] = format(nextPC, "08b")   #dectobin(nextPC)

        return self.to_return
        

