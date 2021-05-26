#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: May 2021
# This program prints the volume of a cylinder
#   user inputs number

import math


def calculate_volume(radius, height):
    # This function prints the volume of a cylinder

    # process
    volume = math.pi * radius ** 2 * height

    return volume


def main():
    # this function just calls other functions

    radius_from_user = input("Enter the radius of a cylinder (mm): ")
    height_from_user = input("Enter the height of a cylinder (mm): ")
    print("")

    try:
        radius_integer = float(height_from_user)
        height_integer = float(radius_from_user)
        volume_of_cylinder = calculate_volume(height_integer, radius_integer)
        print("The volume is cylinder with radius "
              "{0}mm and height {1}mm is {2:,.2f} mm³".
              format(radius_integer, height_integer, volume_of_cylinder))
    except Exception:
        print("{} is not an integer".format(radius_from_user))


if __name__ == "__main__":
    main()
