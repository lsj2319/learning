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

def main():
        # write a program to ask user their height in METERS
        # it will be a float!
        # evaluate if their height is too short or too tall or ok to ride
        # print response depending on evaluation
        # precondition: we don't know if they can ride
        # postcondition: we know if they can ride and tell them.

        # what is their height in meters?
    rider_height = float(input("Enter height in meters: "))
    if (rider_height < 1 or rider_height > 2):
        print("You can't ride the roller coaster.")
    else:
        print("You can ride the roller coaster.")


if __name__ == '__main__':
    main()
