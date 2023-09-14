import cv2
import numpy as np
from lab5a import *

def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    """ Returns a function `is_sky` that takes a pixel as input and
    returns 1 if it falls within the specified constraints, 0 if the pixel is None,
    and None if the pixel is outside the constraints or has invalid format. """
    def is_sky(px):
        if px is None:
            return None  # Return None for None pixels
        try:
            # Check if the pixel falls within the specified color channel constraints
            if hlow <= px[0] <= hhigh and slow <= px[1] <= shigh and vlow <= px[2] <= vhigh:
                return 1
        except (TypeError, IndexError):
            return None  # Return None for pixels with invalid format
        return 0  # Return 0 for pixels that do not meet the constraints
    return is_sky


def greyscale_list_to_cvimg(lst, height, width):
    """ Returnerar en gråskalebild med bredd x höjd och specifikerade pixelvärden. """
    # Skapa en tom bildmatris av typen uint8
    img = np.zeros((height, width), np.uint8)

    # Fyll i pixelvärdena i bildmatrisen
    for x in range(width):
        for y in range(height):
            # Hämta pixelvärdet från listan baserat på positionen (x, y)
            pixel_value = lst[y * width + x]
            # Sätt pixelvärdet i bildmatrisen
            img[y, x] = pixel_value

    return img

"Lab5B2"

def generator_from_image(image_list):
    def generator(index):
        if 0 <= index < len(image_list):
            return image_list[index]
        else:
            return None
    return generator

# Läs in bilden från filen "plane.jpg" och konvertera den till HSV-färgrymden
hsv_plane = cv2.cvtColor(cv2.imread("plane.jpg"), cv2.COLOR_BGR2HSV)

# Konvertera HSV-bilden till en linjär lista av pixelvärden
plane_list = cvimg_to_list(hsv_plane)

# Skapa ett filter för att identifiera himmelpixlar baserat på angivna begränsningar för färgkanalerna
is_sky = pixel_constraint(100, 150, 50, 200, 100, 255)

# Använd filterfunktionen för att mappa över varje pixel i plane_list och skapa en ny lista med 1:or och 0:or
sky_pixels = list(map(lambda x: x * 255, map(is_sky, plane_list)))

# Skapa en svartvit bild baserat på den nya listan med pixelvärden och visa den
cv2.imshow('sky', greyscale_list_to_cvimg(sky_pixels, hsv_plane.shape[0], hsv_plane.shape[1]))
cv2.waitKey( )

