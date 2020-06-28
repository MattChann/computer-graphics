# Work 0: Imagine All the Pixels...

**Due: Monday 02/03 8:00am**

GitHub link: https://github.com/mks66/picmaker.git

Time for your first computer generated image:
1. Create a program that generates a valid ppm image file, it should be at least 500x500, but also don’t make it too big (remember, each pixel is stored as up to 9 bytes - 3 for each color value - so a 1000x1000 image could be 9MB large, they get big fast).
2. Upload your code, as a submodule, to the appropriate place on github.
3. Convert your image to a png and upload it to the ML6 gallery website: http://gallery.stuycs.org
    - For help with converting, you should install ImageMagick
        - on ubuntu: `$ apt-get install imagemagick`
        - on mac:
            - First install XQuartz: https://www.xquartz.org/index.html
            - (if you have homebrew installed): `$ brew install imagemagick --with-x11`
            - If you’re more of a macports kind of person: `$ port install imagemagick`
        - on windows… installing ubuntu and running apt-get install imagemagick will work, but there may be other options as well. for more detailed instructions (including building and installing it on your own): http://www.imagemagick.org/script/binary-releases.php
        - You can also log into any stuy machine remotely, and run convert on them.
    - Once you’ve installed image magic, you can convert with the following command:
        - `$ convert <source> <destination>`
        - example: `$ convert foo.ppm foo.png`
        - The destination format will be automatically set based on the file extension.
4. You must submit your code via github and upload an image!
5. Did you remember to include a makefile?
