// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

	@R0		// initialising the multiplier
	D=M
	@i
	M=D		

	@R1		// initialising the multiplicand
	D=M
	@j
	M=D

	@R2		//initialising the result
	M=0

(LOOP)
	
	@i		
	D=M
	@END		
	D;JLE	// check whether i > 0, else end the program

	@j		
	D=M
	@R2
	M=D+M	// adding the multiplicand to the result multiple times

	@i		
	M=M-1	// decrementing the count 

	@LOOP	// Goto the Label 
	0;JMP

(END)
	@END	// infinite loop
	0;JMP
