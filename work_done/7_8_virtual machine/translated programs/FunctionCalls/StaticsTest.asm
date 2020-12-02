@ 256
D=A
@ SP
M=D
@ $RET__STARTUP:0
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ LCL
D=M
@ SP
A=M
M=D
@ SP
M=M+1
@ ARG
D=M
@ SP
A=M
M=D
@ SP
M=M+1
@ THIS
D=M
@ SP
A=M
M=D
@ SP
M=M+1
@ THAT
D=M
@ SP
A=M
M=D
@ SP
M=M+1
D=M
@ LCL
M=D
@ 5
D=D-A
@ 0
D=D-A
@ ARG
M=D
@ Sys.init
0;JMP
( $RET__STARTUP:0 )
( Sys.init )
@ SP
A=M
D=A
@ SP
M=D
@ 6
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ 8
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ $RET_Sys.init:3
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ LCL
D=M
@ SP
A=M
M=D
@ SP
M=M+1
@ ARG
D=M
@ SP
A=M
M=D
@ SP
M=M+1
@ THIS
D=M
@ SP
A=M
M=D
@ SP
M=M+1
@ THAT
D=M
@ SP
A=M
M=D
@ SP
M=M+1
D=M
@ LCL
M=D
@ 5
D=D-A
@ 2
D=D-A
@ ARG
M=D
@ Class1.set
0;JMP
( $RET_Sys.init:3 )
@ R5
D=A
@ 0
D=D+A
@ SP
M=M-1
A=M+1
M=D
A=A-1
D=M
A=A+1
A=M
M=D
@ 23
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ 15
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ $RET_Sys.init:7
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ LCL
D=M
@ SP
A=M
M=D
@ SP
M=M+1
@ ARG
D=M
@ SP
A=M
M=D
@ SP
M=M+1
@ THIS
D=M
@ SP
A=M
M=D
@ SP
M=M+1
@ THAT
D=M
@ SP
A=M
M=D
@ SP
M=M+1
D=M
@ LCL
M=D
@ 5
D=D-A
@ 2
D=D-A
@ ARG
M=D
@ Class2.set
0;JMP
( $RET_Sys.init:7 )
@ R5
D=A
@ 0
D=D+A
@ SP
M=M-1
A=M+1
M=D
A=A-1
D=M
A=A+1
A=M
M=D
@ $RET_Sys.init:9
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ LCL
D=M
@ SP
A=M
M=D
@ SP
M=M+1
@ ARG
D=M
@ SP
A=M
M=D
@ SP
M=M+1
@ THIS
D=M
@ SP
A=M
M=D
@ SP
M=M+1
@ THAT
D=M
@ SP
A=M
M=D
@ SP
M=M+1
D=M
@ LCL
M=D
@ 5
D=D-A
@ 0
D=D-A
@ ARG
M=D
@ Class1.get
0;JMP
( $RET_Sys.init:9 )
@ $RET_Sys.init:10
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ LCL
D=M
@ SP
A=M
M=D
@ SP
M=M+1
@ ARG
D=M
@ SP
A=M
M=D
@ SP
M=M+1
@ THIS
D=M
@ SP
A=M
M=D
@ SP
M=M+1
@ THAT
D=M
@ SP
A=M
M=D
@ SP
M=M+1
D=M
@ LCL
M=D
@ 5
D=D-A
@ 0
D=D-A
@ ARG
M=D
@ Class2.get
0;JMP
( $RET_Sys.init:10 )
( Sys.init:WHILE )
@ Sys.init:WHILE
0;JMP
( Class1.set )
@ SP
A=M
D=A
@ SP
M=D
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
D=0
@ 18
D=D+A
@ SP
M=M-1
A=M+1
M=D
A=A-1
D=M
A=A+1
A=M
M=D
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
D=0
@ 19
D=D+A
@ SP
M=M-1
A=M+1
M=D
A=A-1
D=M
A=A+1
A=M
M=D
@ 0
D=A
@ SP
A=M
M=D
@ SP
M=M+1
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
( Class1.get )
@ SP
A=M
D=A
@ SP
M=D
D=0
@ 18
A=D+A
D=M
@ SP
A=M
M=D
@ SP
M=M+1
D=0
@ 19
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
( Class2.set )
@ SP
A=M
D=A
@ SP
M=D
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
D=0
@ 20
D=D+A
@ SP
M=M-1
A=M+1
M=D
A=A-1
D=M
A=A+1
A=M
M=D
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
D=0
@ 21
D=D+A
@ SP
M=M-1
A=M+1
M=D
A=A-1
D=M
A=A+1
A=M
M=D
@ 0
D=A
@ SP
A=M
M=D
@ SP
M=M+1
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
( Class2.get )
@ SP
A=M
D=A
@ SP
M=D
D=0
@ 20
A=D+A
D=M
@ SP
A=M
M=D
@ SP
M=M+1
D=0
@ 21
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
