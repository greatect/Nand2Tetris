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
@ 4
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ $RET_Sys.init:2
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
@ Main.fibonacci
0;JMP
( $RET_Sys.init:2 )
( Sys.init:WHILE )
@ Sys.init:WHILE
0;JMP
( Main.fibonacci )
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
@ 2
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
D=M-D
M=-1
@ $LOGIC_Main.fibonacci:0
D;JLT
@ SP
A=M-1
M=0
($LOGIC_Main.fibonacci:0)
@ SP
M=M-1
A=M
D=M
@ Main.fibonacci:IF_TRUE
D;JNE
@ Main.fibonacci:IF_FALSE
0;JMP
( Main.fibonacci:IF_TRUE )
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
( Main.fibonacci:IF_FALSE )
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
@ 2
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
M=M-D
@ $RET_Main.fibonacci:13
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
@ Main.fibonacci
0;JMP
( $RET_Main.fibonacci:13 )
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
@ 1
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
M=M-D
@ $RET_Main.fibonacci:17
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
@ Main.fibonacci
0;JMP
( $RET_Main.fibonacci:17 )
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
