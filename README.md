# Notes for Computer Graphics Class
    
<!-------   Wednesday, January 29, 2020   ------->
### Peering into the depths of color
#### Color Depth
- The amount of data used to represent a single pixel

| size   | color options                           |
| ------ |:---------------------------------------:|
| 1 bit  | 1 color, on \| off                      |
| 2 bit  | 1 color with intensity                  |
| 3 bit  | Red, Green, Blue, on \| off             |
| 4 bit  | RGB with intensity                      |
| 6 bit  | RGB, each color has its own intensity   |
| 3 byte | RGB, each with 256 possible intensities |

#### Other Color Spaces
- RGBA
    - Red, Green, Blue + Alpha (transparency)
- HSB
    - Hue, Saturation, Brightness
    - <img src="https://upload.wikimedia.org/wikipedia/commons/e/ea/HSV_cone.png" alt="HSB Visualization" width="250"/>
#### Image File Formats
- Raster vs. Vector
    - Vector formats represent images as a series of drawing instructions
        - Infinitely scalable
        - SVG (Scalable Vector Graphics)
    - Raster formats represent images as a grid of pixels
- Uncompressed vs. Compressed (Raster)
    - Uncompressed formats contain data for each pixel
        - BMP, TIFF, RAW    <!-------   Thursday, January 30, 2020   ------->
    - Compressed formats use a compression algorithm to minimize file size
    - Lossless vs. Lossy
        - Lossless compression algorithms contain enough information to exactly recreate the image
            - Run Length Encoding
                - `RRRRRGGBBBB` --> `R5G2BB4`
            - PNG (Portable Network Graphics), GIF (Graphics Interchange Format)
        - Lossy compression algortihms do not retain all the details of the original image
            - JPEG (Joint Photographic Experts Group)
#### PPM (Portable PixMap)
- Uncompressed raster format
- Part of NETPBM Graphics family
- Pixel data is represented by RGB triplets in either ASCII or binary
- All whitespace is equivalent
- Ex ASCII ppm file (`pic.ppm`)
```ppm
P3
5 5
255
255 255 0 255 255 0 255 255 0 255 255 0 255 255 0
255 255 0 255 255 0 255 255 0 255 255 0 255 255 0
255 255 0 255 255 0 255 255 0 255 255 0 255 255 0
255 255 0 255 255 0 255 255 0 255 255 0 255 255 0
255 255 0 255 255 0 255 255 0 255 255 0 255 255 0 
```

- Making a PPM file (line-by-line, but all whitespace is equivalent anyways):
    - Must start with `P3` if in ASCII, `P6` if in binary
    - Specify width then height
    - Specify max value (will map 0->255 to 0->100 if you use `100`)
    - Then your pixel triplets
    - Note-to-self: leave the trailing space after last pixel; if not there, will give error about end-of-file when converting

<!-------   Monday, February 03, 2020   ------->
### Line Algorithm
![Line Algorithm Diagram](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQc0kjSOTnP9pxiE3vwlMnmIm9x1jsdqYyRvqh-0UtzIWK1_qrI&s)

**Input**: 2 endpoints

Ideas?:
- test potential pixels
- iterate through potential pixels
- one pixel per x-value*

![Octants Diagram](https://i.stack.imgur.com/Gk616.jpg)

**Octant I**: `0 < m < 1`
