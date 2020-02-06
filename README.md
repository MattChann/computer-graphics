# Work 02: Because it's time, you'll make a line

**Due: Tuesday 02/011 8:00am**

GitHub link: https://github.com/mks66/line.git

You will write your own line algorithm!
1. First decide what you will be programming in for this assignment. You can use any language you’d like, but you must write your own line algorithm (do not use any built in function that may exist for your language of choice).
    - I have provided frameworks for both c and python, these can be found here: https://github.com/mks66/66source
    - Also note the .gitignore file located there, you **should** use it.
    - In order to save an image in a non ppm format, or display the image, you must have _imagemagick_ installed
2. Code Bresenham’s line algorithm!
    - Start with octant 1.
    - Add the other octants one at a time, you’ll have a much easier time debugging doing that. (Trust me, I’ve done this a few times).
3. Test your algorithm by calling your draw_line routine multiple times.
4. Running make should result in displaying/saving an image that tests all octants, including slopes of 0, 1, -1 and undefined slopes.
    - This image does not need to be the same as your gallery image.
5. Don’t forget to upload an image to the gallery!
    - Follow all the submission guidelines at the top of this page.

If you are using my frameworks you only need to modify the following files:
- c
    - draw_c
    - main_c
- python
    - draw.py
    - main.py
