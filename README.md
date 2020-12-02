# Nand2Tetris

## Introduction
This repository contains my work on building a general-purpose computer system, following the course [From Nand to Tetris](https://www.nand2tetris.org). There are several phases in the development of computers I found worth mentioning:
- The designs from semiconductors to transitors to nand gates to flip-flops
- (De)multiplexor gates that are very useful in bringing different parts of the circuit together
- The idea of Memory-mapped IO that simplifies the interaction with peripherals
- Turing machine and Von Neumann architecture that lies at the heart of computer design
- Human-readable assembly codes that marks the first milestone of program development
- Virtual separation of memory sections and the execution of function calls / returns
- The concept of simulating virtual machines that abstracts away hardware-specific constructs
- How high-level languages are possible and related compilation knowledge

## Guides
[project\_files](/project_files) and [software\_tools](/software_tools) directly refer to the software suite provided in the course website.
[work\_done](/work_done) contains my work on all these projects.

To use my assembler, translator and compiler, navigate to the containing folder and run
```
python3 assembler.py  /path/to/file
python3 translator.py /path/to/folder
python3 Compiler.py   /path/to/folder
```
The .hdl, .hack, .vm files can be loaded using the corresponding software in software\_tools.

## License
The referenced software suite is under the GNU GPL (General Public License).
