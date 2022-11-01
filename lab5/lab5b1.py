import cv2
import cvlib
import numpy
import close_openCV
import math


def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    """ Returns a function is_sky that takes a pixel as input and
    returns 1 if it is within the given constraints otherwise 0 """
    def is_sky(px):
        try:
            if px[0] < hhigh and px[0] > hlow and px[1] < shigh and \
                px[1] > slow and px[2] < vhigh and px[2] > vlow:
                return 1
        except TypeError:
            return None
        except IndexError:
            return None
        return 0
    return is_sky

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

img= cv2.cvtColor(cv2.imread("plane.jpg"), cv2.COLOR_BGR2HSV)
cvlist = cvimg_to_list(hsv_plane)

is_sky = pixel_constraint(100, 150, 50, 200, 100, 255)
sky_pixels = list(map(lambda x: x * 255, map(is_sky, plane_list)))

cv2.imshow('sky', greyscale_list_to_cvimg(sky_pixels, hsv_plane.shape[0], hsv_plane.shape[1]))
cv2.waitKey(0)


    

