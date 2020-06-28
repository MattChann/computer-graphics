# Work 02: Enter the Matrix

**Due: Monday 02/24 8:00am**

GitHub link: https://github.com/mks66/matrix.git

Implement the following features but you cannot trivialize the problem by using a structure that already exists in the language you choose:
- General Matrix stuff
    - matrix multiplication
    - creation of an identity matrix
    - displaying a matrix in a reasonable manner
- Graphics matrix stuff
    - add a point to an edge matrix
    - add an edge to an edge matrix (should call your add point routine)
    - go through an edge matrix and draw the lines stored in the matrix (should call your draw line routine)
- Create a main function/method that demonstrates all the of matrix routines you wrote, and generates an image using the edge matrix structure. Upload the image to the gallery page.
- READ THROUGH ALL THE SOURCE FILES. Detailed instructions are provided as comments.

Here is an example of output, including a correct matrix multiplication:
```
Testing add_edge. Adding (1, 2, 3), (4, 5, 6) m2 =
1.00 4.00
2.00 5.00
3.00 6.00
1.00 1.00

Testing ident. m1 =
1.00 0.00 0.00 0.00
0.00 1.00 0.00 0.00
0.00 0.00 1.00 0.00
0.00 0.00 0.00 1.00

Testing Matrix mult. m1 * m2 =
1.00 4.00
2.00 5.00
3.00 6.00
1.00 1.00

Testing Matrix mult. m1 =
1.00 4.00 7.00 10.00
2.00 5.00 8.00 11.00
3.00 6.00 9.00 12.00
1.00 1.00 1.00 1.00

Testing Matrix mult. m1 * m2 =
40.00 76.00
47.00 92.00
54.00 108.00
7.00 16.00
```
