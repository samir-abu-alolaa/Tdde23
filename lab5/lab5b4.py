import cv2
import numpy as np
from lab5a import cvimg_to_list, rgblist_to_cvimg

def blend_condition(pixel):
    # Beräkna det genomsnittliga gråvärdet för pixeln
    gray = sum(pixel) // 3
    # Konvertera gråvärdet till en konditionsparameter mellan 0 och 1
    return gray / 255.0

def generator_from_image(image_list):
    def generator(index):
        if 0 <= index < len(image_list):
            return image_list[index]
        else:
            return None
    return generator

def combine_images(image_list, condition, generator1, generator2, generator3):
    result = []
    for i, pixel in enumerate(image_list):
        cond = condition(pixel)
        gen1 = generator1(i)
        gen2 = generator2(i)
        gen3 = generator3(i)
        combined_pixel = tuple(int(c1 * cond + c2 * (1 - cond)) for c1, c2 in zip(gen1, gen2))
        result.append(combined_pixel)
    return result

# Läs in originalbilderna
flower_img = cv2.imread("flowers.jpg")
plane_img = cv2.imread("plane.jpg")
gradient_img = cv2.imread("gradient.jpg")

# Konvertera bilderna till en lista av BGR-pixlar
flower_img_list = cvimg_to_list(flower_img)
plane_img_list = cvimg_to_list(plane_img)
gradient_img_list = cvimg_to_list(gradient_img)

# Skapa generatorfunktioner från listorna med bilder
generator1 = generator_from_image(flower_img_list)
generator2 = generator_from_image(plane_img_list)
generator3 = generator_from_image(gradient_img_list)

# Definiera konditionsfunktionen baserad på gråskalan
condition = blend_condition

# Kombinera bilderna med hjälp av konditionsfunktionen
result = combine_images(gradient_img_list, condition, generator1, generator2, generator3)

# Konvertera resultatet till en numpy-matris
new_img = rgblist_to_cvimg(result, gradient_img.shape[0], gradient_img.shape[1])

# Visa den slutliga bilden
cv2.imshow('Slutlig bild', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
