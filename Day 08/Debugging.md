
## Common Debugger  Commands

Command            Action
n or next              Run the next line of code
s or step               Step into a function call
c or continue        Continue running until the next breakpoint or end
l or list                   List the surrounding code lines
p or print              Print the value of a variable 
quit                Exit the debugger


## Inspecting Variable

- While paused at a breakpoint, you can check the value of variables

(Pdb) x
10
(Pdb) y
5 (Pdb) result

NameError: name 'result' is not defned

- You can also change variable values to test different scenarios:
(Pdb) x = 20
(Pdb) n

## Stepping Through Code

- Use n (next) to execute the next line
- Use s (step) to step into a function call
- Use c (continue) to run until the next breakpoint or end the program


## Tips for effective Debugging

