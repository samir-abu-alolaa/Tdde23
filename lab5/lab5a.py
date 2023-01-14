import cv2
import numpy
def cvimg_to_list(img):
    shape = img.shape
    row = shape[0]
    kolumner = shape[1]
    lst=[]
    for x in range(row):
        for y in range(kolumner):
            ans = tuple(img[x,y])
            lst.append(ans)
    return lst

def rgblist_to_cvimg(lst, height, width):
    """Return a width x height OpenCV image with specified pixels."""
    # A 3d array that will contain the image data
    img = numpy.zeros((height, width, 3), numpy.uint8)

    for x in range(0, width):
        for y in range(0, height):
            pixel = lst[y * width + x]
            img[y, x, 0] = pixel[0]
            img[y, x, 1] = pixel[1]
            img[y, x, 2] = pixel[2]

    return img
img = cv2.imread("Baki.jpg")
list_img =cvimg_to_list(img)
converted_img = rgblist_to_cvimg(list_img, img.shape[0], img.shape[1])
cv2.imshow("converted", converted_img)
cv2.waitKey(0)