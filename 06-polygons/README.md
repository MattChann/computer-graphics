# Work 06: If your shapes don't look solid, TRI a different ANGLE

Due: Monday 03/30 10:00am

GitHub link: https://github.com/mks66/polygons.git

- Relevant notes: Sections 1-3
- The Drawing:
    - Create new functions to add a polygon to a matrix, and go through the matrix 3 points at a time to draw triangles.
    - You should have a new triangle matrix that exists alongside the edge matrix. The edge matrix should be used for the shapes that are exclusively 2d (lines, circles, splines), and the triangle matrix for our 3d shapes.
    - Anything aside from shape drawing that modifies/uses the edge matrix (apply, clear, display, save) should now modify/use the triangle matrix as well.
    - Modify add box, add sphere and add torus to add triangles instead of points.
    - Make sure the parser calls the draw_polygons functions when needed instead of draw_lines

**NEW ADDITION**
- Relevant notes: Sections 4-5
- Implement the following vector functions
- Find the dot product of 2 vectors (provided as arrays/lists of 3 values)
- Calculate the surface normal of a triangle in the polygon matrix (provided the polygon matrix and index.
- Check out gmath.h/c or gmath.py for headers and comments.
    - There are funtion headers listed for normalizing a vector, you can ignore those if you want.
    - We won’t be needing that functionality until we get to lighting & shading.
- Implement Backface culling.
