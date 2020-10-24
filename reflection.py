"""
File: reflection.py
----------------
Take an image. Generate a new image with twice the height. The top half
of the image is the same as the original. The bottom half is the mirror
reflection of the top half.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage


def make_reflected(filename):
    image = SimpleImage(filename)
    # precondition: photo of an image
    # postcondition: new image with the original and reflection
    width = image.width
    height = image.height

    # create a reflect variable to store the new image that is twice as high
    reflect = SimpleImage.blank(width, height * 2)

    for y in range(height):
            for x in range(width):
                pixel = image.get_pixel(x,y)
                reflect.set_pixel(x, y, pixel)
                reflect.set_pixel(x, (height *2) - (y+1), pixel)
    # return new image
    return reflect

def main():
    """
    This program tests your make_reflected function by displaying
    the original image  as well as the resulting image
    from your make reflected function.
    """
    original = SimpleImage('images/mt-rainier.jpg')
    original.show()
    reflected = make_reflected('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
