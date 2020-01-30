# Notes for Computer Graphics Class
    
<!-------   Wednesday, January 29, 2020   ------->

## Peering into the depths of color
### Color Depth
- The amount of data used to represent a single pixel

| size   | color options                           |
| ------ |:---------------------------------------:|
| 1 bit  | 1 color, on \| off                      |
| 2 bit  | 1 color with intensity                  |
| 3 bit  | Red, Green, Blue, on \| off             |
| 4 bit  | RGB with intensity                      |
| 6 bit  | RGB, each color has its own intensity   |
| 3 byte | RGB, each with 256 possible intensities |

### Other Color Spaces
- RGBA
    - Red, Green, Blue + Alpha (transparency)
- HSB
    - Hue, Saturation, Brightness
    - ![HSB Visualization](https://upload.wikimedia.org/wikipedia/commons/e/ea/HSV_cone.png "HSB Visualization")
### Image File Formats
- Raster vs. Vector
    - Vector formats represent images as a series of drawing instructions
        - Infinitely scalable
        - SVG (Scalable Vector Graphics)
    - Raster formats represent images as a grid of pixels
- Uncompressed vs. Compressed (Raster)
    - Uncompressed formats contain data for each pixel
        - BMP, TIFF, RAW
