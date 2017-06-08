// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(LOOP)
	@KBD 		// base address of keyboard mapping
	D=M			// get value stored in the keyboard reg
	@WHITE		
	D; JEQ		// jump to White label if no key is pressed

	@i
	M=0			// i = 8191, the number of registers(+1) to be set.

(BLACK)
	@i		
	D=M			// D = i
	@256
	D=D-A		// D = i - 256
	@LOOP
	D; JGE		// if (i - 256) >= 0, loop back

	@SCREEN
	A=D+M		// A = base + i; Accessing the RAM[base+i]
	M=-1			// decimal equivalent of Ox00 = Black
	A=A+1
	M=-1
	A=A+1
	M=-1
	A=A+1
	M=-1
	A=A+1
	M=-1
	A=A+1
	M=-1
	A=A+1
	M=-1
	A=A+1
	M=-1
	A=A+1
	M=-1
	A=A+1
	M=-1
	A=A+1
	M=-1
	A=A+1
	M=-1
	A=A+1
	M=-1
	A=A+1
	M=-1
	A=A+1
	M=-1
	A=A+1
	M=-1
	
	//i++
	@i
	M=M+1

	// loop back to black
	@BLACK
	0; JEQ		

	@i
	M=0			// i = 8191, the number of registers(+1) to be set.

(WHITE)
	@i		
	D=M			// D = i
	@256
	D=D-A		// D = i - 256
	@LOOP
	D; JGE		// if (i - 256) >= 0, loop back

	@SCREEN
	A=D+M		// A = base + i; Accessing the RAM[base+i]
	M=0			// decimal equivalent of Ox00 = WHITE
	A=A+1
	M=0
	A=A+1
	M=0
	A=A+1
	M=0
	A=A+1
	M=0
	A=A+1
	M=0
	A=A+1
	M=0
	A=A+1
	M=0
	A=A+1
	M=0
	A=A+1
	M=0
	A=A+1
	M=0
	A=A+1
	M=0
	A=A+1
	M=0
	A=A+1
	M=0
	A=A+1
	M=0
	A=A+1
	M=0

	//i++
	@i
	M=M+1

	// loop back to WHITE
	@WHITE
	0; JEQ		
