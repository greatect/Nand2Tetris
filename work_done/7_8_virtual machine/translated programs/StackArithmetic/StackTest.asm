@ 17
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ 17
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
@ __LOGIC:$0
D;JEQ
@ SP
A=M-1
M=0
(__LOGIC:$0)
@ 17
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ 16
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
@ __LOGIC:$1
D;JEQ
@ SP
A=M-1
M=0
(__LOGIC:$1)
@ 16
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ 17
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
@ __LOGIC:$2
D;JEQ
@ SP
A=M-1
M=0
(__LOGIC:$2)
@ 892
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ 891
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
@ __LOGIC:$3
D;JLT
@ SP
A=M-1
M=0
(__LOGIC:$3)
@ 891
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ 892
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
@ __LOGIC:$4
D;JLT
@ SP
A=M-1
M=0
(__LOGIC:$4)
@ 891
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ 891
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
@ __LOGIC:$5
D;JLT
@ SP
A=M-1
M=0
(__LOGIC:$5)
@ 32767
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ 32766
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
@ __LOGIC:$6
D;JGT
@ SP
A=M-1
M=0
(__LOGIC:$6)
@ 32766
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ 32767
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
@ __LOGIC:$7
D;JGT
@ SP
A=M-1
M=0
(__LOGIC:$7)
@ 32766
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ 32766
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
@ __LOGIC:$8
D;JGT
@ SP
A=M-1
M=0
(__LOGIC:$8)
@ 57
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ 31
D=A
@ SP
A=M
M=D
@ SP
M=M+1
@ 53
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
@ 112
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
@ SP
A=M-1
M=-M
@ SP
M=M-1
A=M
D=M
A=A-1
M=M&D
@ 82
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
M=M|D
@ SP
A=M-1
M=!M
