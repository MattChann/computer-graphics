# Work 10: More Delightful Labor

Due: Monday 05/04 10:00am

GitHub link: https://github.com/mks66/mdl.git

(MDL actually stands for Motion Description Language)
- Before doing anything else, take a look at MDL.spec, it provides important information about the language structure.
- There are many commands and features in MDL that we will not be using yet, you should ignore those for now.

Implement the following mdl commands:
- push
    - push a copy of the current top of the origins stack onto the origins stack (a full copy, not just a reference to the current top)
- pop
    - removes the top of the origins stack (nothing needs to be done with this data)
- move/rotate/scale
    - create a translation/rotation/scale matrix and multiply the current top by it
    - do not try to use the optional arguments for these commands
- box/sphere/torus
    - add a box/sphere/torus to a temporary polygon matrix, multiply it by the current top and draw it to the screen
    - if a constants variable is present, use those for lighting, otherwise, use a default set.
    - ignore the optional variable at the end of the command.
- constants
    - you actually don’t need to do anything for this command, the semantic analyzer will already create a symbol table entry for the reflective constants.
- line
    - add a line to a temporary edge matrix, multiply it by the current top and draw it to the screen
    - do not try to use the optional arguments for this command
- save
    - save the screen to the provided file name
- display
    - show the image
- You only need to modify one of the following files (c/python):
    - C
        - my_main.c
        - look at print_pcode.c, it is an ideal template to follow for my_main.c
        - mdl.y: there is a comment at the very bottom that you will need to check.
    - Python
        - script.py
