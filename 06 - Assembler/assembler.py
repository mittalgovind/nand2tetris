# assembler.py
# this is an assembler for converting the 
# HACK language code to machine language.
# Please refer to nand2tetris.org for more details.

# def main(s):
import re
import os

def atobin(inst):
    binary = ""
    while inst != 0 :
        binary = str(inst % 2) + binary
        inst = int(inst / 2)
    binary = '{:0>16}'.format(binary)
    return binary

def ctobin(inst):
    binary = "111"
    dest = inst.group(1)
    comp = inst.group(2)
    jump = inst.group(3)
    dest_bits = ""
    comp_bits = ""
    jump_bits = ""
    
    if comp == '':
        comp = dest
        dest_bits = "000"
    else:
        if dest.find('A') != -1 :
            dest_bits += "1"
        else: 
            dest_bits += "0"

        if dest.find('D') != -1 :
            dest_bits += "1"
        else: 
            dest_bits += "0"

        if dest.find('M') != -1 :
            dest_bits += "1"
        else: 
            dest_bits += "0"

    if jump == '' or jump == "  ":
        jump_bits = "000"
    else:
        if jump == 'JMP':
            jump_bits = "111"
        else:
            if jump == 'JGT':
                jump_bits = "001"
            else:
                if jump == 'JEQ':
                    jump_bits = "010"
                else:
                    if jump == 'JGE':
                        jump_bits = "011"
                    else:
                        if jump == 'JLT':
                            jump_bits = "100"
                        else:
                            if jump == 'JNE':
                                jump_bits = "101"
                            else:
                                if jump == 'JLE':
                                    jump_bits = "110"


    if comp.find('M') != -1:
        comp_bits += "1"
        if comp == 'M':
            comp_bits += "110000"
        else: 
            if comp == "!M":
                comp_bits += "110001"
            else: 
                if comp == "-M":
                    comp_bits += "110011"
                else: 
                    if comp == "M+1":
                        comp_bits += "110111"
                    else: 
                        if comp == "M-1":
                            comp_bits += "110010"
                        else: 
                            if comp == "D+M":
                                comp_bits += "000010"
                            else: 
                                if comp == "D-M":
                                    comp_bits += "010011"
                                else: 
                                    if comp == "M-D":
                                        comp_bits += "000111"
                                    else: 
                                        if comp == "D&M":
                                            comp_bits += "000000"
                                        else: 
                                            if comp == "D|M":
                                                comp_bits += "010101" 
    else :
        comp_bits += "0"
        if comp == "A":
            comp_bits += "110000"
        else: 
            if comp == "!A":
                comp_bits += "110001"
            else: 
                if comp == "-A":
                    comp_bits += "110011"
                else: 
                    if comp == "A+1":
                        comp_bits += "110111"
                    else: 
                        if comp == "A-1":
                            comp_bits += "110010"
                        else: 
                            if comp == "D+A":
                                comp_bits += "000010"
                            else: 
                                if comp == "D-A":
                                    comp_bits += "010011"
                                else: 
                                    if comp == "A-D":
                                        comp_bits += "000111"
                                    else: 
                                        if comp == "D&A":
                                            comp_bits += "000000"
                                        else: 
                                            if comp == "D|A":
                                                comp_bits += "010101" 
                                            else: 
                                                if comp == "0":
                                                    comp_bits += "101010" 
                                                else: 
                                                    if comp == "1":
                                                        comp_bits += "111111" 
                                                    else: 
                                                        if comp == "-1":
                                                            comp_bits += "111010" 
                                                        else: 
                                                            if comp == "D":
                                                                comp_bits += "001100" 
                                                            else: 
                                                                if comp == "-D":
                                                                    comp_bits += "001111" 
                                                                else: 
                                                                    if comp == "!D":
                                                                        comp_bits += "001101" 
                                                                    else: 
                                                                        if comp == "D+1":
                                                                            comp_bits += "011111" 
                                                                        else: 
                                                                            if comp == "D-1":
                                                                                comp_bits += "001110"
    binary += comp_bits + dest_bits + jump_bits
    return binary

def main():
	filename = input("Please go to the directory the file is and enter its full name (File.asm): ")
	# regex expression for capturing the A, C instructions and Labels together
	regex_A = re.compile(r"@([A-Za-z0-9_.\$]+)") 
	regex_C = re.compile(r"([AMD0]+)=?([AMD]*\+?-?&?\|?!?[AMD01]*);?(JGT|JEQ|JGE|JLT|JNE|JLE|JMP|)")
	regex_label = re.compile(r"\([ ]*([A-Za-z0-9_.\$]+)[ ]*\)")

	# making the symbol table with pre-defined symbols
	symbols = {}

	# adding the predefined symbols R0 to R15
	for i in range(16):
	    symbols["R%d"%i] = i
	symbols["SP"] = 0
	symbols["LCL"] = 1
	symbols["ARG"] = 2
	symbols["THIS"] = 3
	symbols["THAT"] = 4
	symbols["SCREEN"] = 16384
	symbols["KBD"] = 24576

	# table containing labels
	labels = {}
	# starting address of variable declaration = RAM[16]
	n = 16

	# number of lines of code processed
	processed = 0
	cwd = os.getcwd()
	output = open(cwd + "/temp.hack", "w")
	with open(cwd +"/" + filename, "r") as f :
	    for line in f:
	        # if the line contains a comment only take the part before it
	        if line.find("//") != -1:
	            line = line.split("//")[0]
	        match_A = re.search(regex_A, line)
	        match_C = re.search(regex_C, line)
	        match_labels = re.search(regex_label, line)
	        
	#       Note the priority of matching is important
	        if match_A:
	            output.write(match_A.group(0) + "\n")
	#             print("added alpha by specified " + match_A.group(1) + " to " + str(symbols[match_A.group(1)]))
	            processed += 1

	        else: 
	            if match_labels:
	                    labels[match_labels.group(1)] = processed
	#                     print("added label " + match_labels.group(1) + " to " + str(processed))
	            else:
	                if match_C:
	                    output.write(match_C.group() + "\n")
	                    processed += 1
	output.close()
	output = open(cwd + "/temp.hack", "r")
	# second pass
	conv = open(cwd + "/{}.hack".format(filename.split(".asm")[0]), "w")
	for line in output:
	    if line.startswith("@"):
	        # handling A-instruction
	        match_A = re.search(regex_A, line)
	        # covering case if operand is already in the symbol table
	        if match_A.group(1) in symbols:
	            a_inst = symbols[match_A.group(1)]
	        else: 
	            # covering the case if operand is a number
	            if match_A.group(1).isdigit():
	                a_inst = int(match_A.group(1))
	            else:
	                # covering case if operand is already in the label table
	                if match_A.group(1) in labels: 
	                    a_inst = labels[match_A.group(1)]
	                else:
	                    while n in symbols.values():
	                        n += 1
	                    symbols[match_A.group(1)] = n
	#                     print("added alpha by n " + match_A.group(1) + " to " + str(n))
	                    a_inst = n
	                    n += 1

	        conv.write(atobin(a_inst) + "\n")
	    else:
	        match_C = re.search(regex_C, line)
	        conv.write(ctobin(match_C) + "\n")
	        
	conv.close()
	os.remove(cwd + "/temp.hack")


main()