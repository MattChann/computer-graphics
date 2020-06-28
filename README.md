# Work 07: Let's see how your code stacks up to the competition

Due: Monday 04/06 10:00am

GitHub link: https://github.com/mks66/cstack.git

Note: If you are working in c, I have provided a basic stack library that you can use in the 66source repository

Time to implement a relative coordinate system… system, add/modify your current parser so it has the following behavior
- `push`
    - Push a copy of the current top of the coordinate system (cs) stack onto the cs stack (a full copy, not just a reference to the current top… I’m looking at you python people)
- `pop`
    - Removes the top of the cs stack (nothing needs to be done with this data)
- `move`/`rotate`/`scale`
    1. create a translation/rotation/scale matrix
    2. multiply the current top of the cs stack by it
    3. The ordering of multiplication is important here. (see notes)
- `box`/`sphere`/`torus`
    1. add a box/sphere/torus to a temporary polygon matrix
    2. multiply it by the current top of the cs stack
    3. draw it to the screen
    4. clear the polygon matrix
- `line`/`curve`/`circle`
    1. add a line to a temporary edge matrix
    2. multiply it by the current top
    3. draw it to the screen (note a line is not a solid, so avoid draw_polygons)
    4. clear the edge matrix
- `save`
    - save the screen with the provided file name
- `display`
    - show the image
- Also note that the `ident`, `apply` and `clear` commands no longer have any use
