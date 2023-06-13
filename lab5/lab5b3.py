import cv2
import random
import numpy as np

def generator_from_image(image_list):
    def generator(index):
        return image_list[index]
    return generator

def cvimg_to_list(img):
    """
    Converts image to list
    """
    height = img.shape[0]
    width = img.shape[1]
    cvlist = []
    try:
        for y in range(height):
            for x in range(width):
                cvlist.append((img[y, x][0], img[y, x][1], img[y, x][2]))
    except TypeError:
        return None
    except IndexError:
        return None

    return cvlist

def rgblist_to_cvimg(lst, height, width):
    """Return a width x height OpenCV image with specified pixels."""
    # A 3d array that will contain the image data
    img = np.zeros((height, width, 3), np.uint8)

    for x in range(0, width):
        for y in range(0, height):
            pixel = lst[y * width + x]
            img[y, x, 0] = pixel[0]
            img[y, x, 1] = pixel[1]
            img[y, x, 2] = pixel[2]

    return img

def combine_images(image_list, condition, generator1, generator2):
    result = []
    for i, pixel in enumerate(image_list):
        cond = condition(pixel)
        gen1 = generator1(i)
        gen2 = generator2(i)
        combined_pixel = tuple(int(c1 * cond + c2 * (1 - cond)) for c1, c2 in zip(gen1, gen2))
        result.append(combined_pixel)
    return result

def gradient_condition(pixel):
    gray = sum(pixel) // 3
    return gray / 255

# Läs in originalbilderna från fil
flower_img = cv2.imread("flower.jpg")
plane_img = cv2.imread("plane.jpg")
gradient_img = cv2.imread("gradient.jpg")

# Skapa generatorer för varje bild
generator1 = generator_from_image(cvimg_to_list(gradient_img))
generator2 = generator_from_image(cvimg_to_list(plane_img))

# Skapa ett filter baserat på gråskala för gradientbilden
condition = gradient_condition

# Kombinera bilderna med den mjuka övergången
result = combine_images(cvimg_to_list(flower_img), condition, generator1, generator2)

# Konvertera resultatet till en bild och visa upp den
new_img = rgblist_to_cvimg(result, flower_img.shape[0], flower_img.shape[1])
cv2.imshow('Final image', new_img)
cv2.waitKey(0)