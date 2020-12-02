( Sys.init )
@ SP
A=M
D=A
@ SP
M=D
@ 4000
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ R3
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
@ 5000
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ R3
D=A
@ 1
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
@ $RET_Sys.init:5
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
@ Sys.main
0;JMP
( $RET_Sys.init:5 )
@ R5
D=A
@ 1
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
( Sys.init:LOOP )
@ Sys.init:LOOP
0;JMP
( Sys.main )
@ SP
A=M
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
D=A
@ SP
M=D
@ 4001
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ R3
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
@ 5001
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ R3
D=A
@ 1
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
@ 200
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ LCL
D=M
@ 1
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
@ 40
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ LCL
D=M
@ 2
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
@ 6
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ LCL
D=M
@ 3
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
@ 123
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ $RET_Sys.main:21
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
@ 1
D=D-A
@ ARG
M=D
@ Sys.add12
0;JMP
( $RET_Sys.main:21 )
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
@ LCL
D=M
@ 2
A=D+A
D=M
@ SP
A=M
M=D
@ SP
M=M+1
@ LCL
D=M
@ 3
A=D+A
D=M
@ SP
A=M
M=D
@ SP
M=M+1
@ LCL
D=M
@ 4
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
M=M-1
A=M
D=M
A=A-1
M=M+D
@ SP
M=M-1
A=M
D=M
A=A-1
M=M+D
@ SP
M=M-1
A=M
D=M
A=A-1
M=M+D
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
( Sys.add12 )
@ SP
A=M
D=A
@ SP
M=D
@ 4002
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ R3
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
@ 5002
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ R3
D=A
@ 1
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
@ 0
A=D+A
D=M
@ SP
A=M
M=D
@ SP
M=M+1
@ 12
D=A
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
