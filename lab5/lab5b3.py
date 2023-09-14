import cv2
import numpy as np
import random
from lab5a import cvimg_to_list, rgblist_to_cvimg

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
def generator_from_image(image_list):
    def generator(index):
        if 0 <= index < len(image_list):
            return image_list[index]
        else:
            return None
    return generator

# Läs in en bild
plane_img = cv2.imread("plane.jpg")

# Konvertera bilden till en NumPy-array
plane_img_array = np.array(plane_img)

# Skapa ett filter som identifierar himlen
condition = pixel_constraint(100, 150, 50, 200, 100, 255)

# Omvandla originalbilden till en lista med HSV-färger
hsv_list = cvimg_to_list(cv2.cvtColor(plane_img, cv2.COLOR_BGR2HSV))
plane_img_list = cvimg_to_list(plane_img)

# Skapa en generator som gör en stjärnhimmel
def generator1(index):
    val = random.random() * 255 if random.random() > 0.99 else 0
    return (val, val, val)


def combine_images(image_list, condition, generator1, generator2):
    result = []
    if len(image_list) == 0:
        return result  # Return empty list if image_list is empty

    if len(image_list) == 1:
        pixel = image_list[0]
        if condition(pixel):
            return [generator1(
                0)]  # Return generator1 result if image_list has a single pixel and it satisfies the condition
        else:
            return [generator2(
                0)]  # Return generator2 result if image_list has a single pixel and it doesn't satisfy the condition


    for i, pixel in enumerate(image_list):
        if condition(pixel):
            result.append(generator1(i))
        else:
            result.append(generator2(i))
    return result


# Skapa en generator för den inlästa bilden
generator2 = generator_from_image(plane_img_list)

# Kombinera de två bilderna till en, alltså använd himmelsfiltret som mask
result = combine_images(hsv_list, condition, generator1, generator2)

# Omvandla resultatet till en riktig bild och visa upp den
new_img = rgblist_to_cvimg(result, plane_img.shape[0], plane_img.shape[1])
cv2.imshow('Final image', new_img)
cv2.waitKey(0)

