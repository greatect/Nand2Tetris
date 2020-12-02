( SimpleFunction.test )
@ SP
A=M
M=0
A=A+1
M=0
A=A+1
D=A
@ SP
M=D
@ LCL
D=M
@ 0
A=D+A
D=M
@ SP
A=M
M=D
@ SP
M=M+1
@ LCL
D=M
@ 1
A=D+A
D=M
@ SP
A=M
M=D
@ SP
M=M+1
@ SP
M=M-1
A=M
D=M
A=A-1
M=M+D
@ SP
A=M-1
M=!M
@ ARG
D=M
@ 0
A=D+A
D=M
@ SP
A=M
M=D
@ SP
M=M+1
@ SP
M=M-1
A=M
D=M
A=A-1
M=M+D
@ ARG
D=M
@ 1
A=D+A
D=M
@ SP
A=M
M=D
@ SP
M=M+1
@ SP
M=M-1
A=M
D=M
A=A-1
M=M-D
@ SP
D=M
@ R14
M=D
@ ARG
D=M
@ SP
M=D+1
@ LCL
D=M
@ R15
M=D-1
A=M
D=M
@ THAT
M=D
@ R15
M=M-1
A=M
D=M
@ THIS
M=D
@ R15
M=M-1
A=M
D=M
@ ARG
M=D
@ R15
M=M-1
A=M
D=M
@ LCL
M=D
@ R15
M=M-1
A=M
D=M
@ R14
A=M
M=D
A=A-1
D=M
@ SP
A=M-1
M=D
@ R14
A=M
A=M
0;JMP
