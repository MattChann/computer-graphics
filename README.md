# Work 08: Scanning for signs of life

Due: Monday 04/13 10:00am

GitHub link: https://github.com/mks66/solids.git

Add scanline conversion and z-buffering to your graphics engine.

Scanline conversion
- Create a new function that handles the scanline conversion.
- Call this in your draw_polygons function.
- Make sure that you change color values for each triangle.
- You may also want to write a sepcial function dedicated to drawing scanlines, feel free to do so.

z-buffering
- In the base files provided, I’ve added a z-buffer argument to the necessary functions, but have not done anything with it.
- The z-buffer should only be modified in your plot function, or when clear_zbuffer is called.
- You will need to calculate z values in both scanline_convert and draw_line (and your draw_scanline function, if you wrote one)
- Your z values are not limited to the integers.

Parser Note:
- In the previous assignment, I noted that the clear command was no longer needed, because we immediately clear the polygon/edge matrix after a shape is drawn. In order to test Scanline conversion on multiple shapes, a different version of clear is useful. Now, clear will clear the screen and zbuffer, allowing us to reset and test multiple shapes in the same script.
- I have added this command to the provided source code, but everyone should implement it.
