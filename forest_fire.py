"""
File: forestfire.py
----------------
This program highlights fires in an image by identifying
pixels who red intensity is more than INTENSITY_THRESHOLD times
the average of the red, green, and blue values at a pixel.
Those "sufficiently red" pixels are then highlighted in the
image and the rest of the image is turned grey, by setting the
pixels red, green, and blue values all to be the same average
value.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage

DEFAULT_FILE = 'images/greenland-fire.png'
RED_COLOR = 255
INTENSITY_THRESHOLD = 1.6

def find_flames(filename):
    """
    This function should highlight the "sufficiently red" pixels
    in the image and grayscale all other pixels in the image
    in order to highlight areas of wildfires.
    """
    image = SimpleImage(filename)
    # precondition: regular image, no fires highlighted
    # postcondition: grayscale image with red where fires are
    # first - check for red enough pixels that could indicate fires
    for pixel in image:
        avg = get_average(pixel) # See if this pixel is "sufficiently" red
        if pixel.red >= avg: # If so,set the red enough pixels to red = 255, then green and blue to 0
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else: # all over pixel set to grayscale
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return image

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the original fire
    original_fire = SimpleImage(filename)
    original_fire.show()

    # Show the highlighted fire
    highlighted_fire = find_flames(filename)
    highlighted_fire.show()

    
def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename

def get_average(pixel):
# use integer divide on rgb values
# Precondition: we don't know the average for each pixel
# Postcondition: we return the average for each pixel
    average = (pixel.blue + pixel.green + pixel.red) // 3
    return average

if __name__ == '__main__':
    main()
