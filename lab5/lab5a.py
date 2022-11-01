import cv2
import numpy as np

def to_list(image):
    rad, kolumn, kanaler = image.shape
    töm_list= []
    for y in range(rad):
        töm_list.append([])
        for x in range(kolumn):
            c = im[y,x]
            tup = (c[2], c[1], c[0])
            töm_list[y].append(tup)
    return töm_list

def rgblist_to_cvimg(lst, height, width):
    """Return a width x height OpenCV image with specified pixels."""
    # A 3d array that will contain the image data
    image = numpy.zeros((height, width, 3), numpy.uint8)

    for x in range(0, width):
        for y in range(0, height):
            pixel = lst[y * width + x]
            img[y, x, 0] = pixel[0]
            img[y, x, 1] = pixel[1]
            img[y, x, 2] = pixel[2]

    return img

im = cv2.imread("Baki.jpg")
