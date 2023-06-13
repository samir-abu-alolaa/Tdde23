import cv2
import random
import numpy

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
    img = numpy.zeros((height, width, 3), numpy.uint8)

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
        if condition(pixel):
            result.append(generator1(i))
        else:
            result.append(generator2(i))
    return result

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

# Läs in originalbilden från fil
plane_img = cv2.imread("plane.jpg")

# Skapa ett filter som identifierar himlen
condition = pixel_constraint(100, 150, 50, 200, 100, 255)

# Omvandla originalbilden till en lista med HSV-färger
hsv_list = cvimg_to_list(cv2.cvtColor(plane_img, cv2.COLOR_BGR2HSV))
plane_img_list = cvimg_to_list(plane_img)

def generator1(index):
    val = random.random() * 255 if random.random() > 0.99 else 0
    return (val, val, val)

generator2 = generator_from_image(plane_img_list)

result = combine_images(hsv_list, condition, generator1, generator2)

new_img = rgblist_to_cvimg(result, plane_img.shape[0], plane_img.shape[1])
cv2.imshow('Final image', new_img)
cv2.waitKey(0)

def test_pixel_constraint():
    # Testfall 1: Testa en pixel som är inom gränserna för himmelfärg
    assert pixel_constraint(100, 150, 50, 200, 100, 255)((120, 100, 150)) == 1
    # Förväntat resultat: Funktionen bör returnera 1 eftersom pixeln ligger inom det angivna färgintervallet.

    # Testfall 2: Testa en pixel som är utanför gränserna för himmelfärg
    assert pixel_constraint(100, 150, 50, 200, 100, 255)((200, 50, 100)) == 0
    # Förväntat resultat: Funktionen bör returnera 0 eftersom pixeln inte ligger inom det angivna färgintervallet.

    # Testfall 3: Testa en pixel med ogiltig färg (None)
    assert pixel_constraint(100, 150, 50, 200, 100, 255)(None) == None
    # Förväntat resultat: Funktionen bör returnera None eftersom pixeln har ogiltig färg och inte kan bedömas.

    # Testfall 4: Testa en pixel med ogiltig färg (felaktig index)
    assert pixel_constraint(100, 150, 50, 200, 100, 255)((200, 50)) == None
    # Förväntat resultat: Funktionen bör returnera None eftersom pixeln har ogiltig färg och inte kan bedömas på grund av felaktigt index.

    # Testfall 5: Testa en pixel som ligger precis vid den övre gränsen för himmelfärg
    assert pixel_constraint(100, 150, 50, 200, 100, 255)((150, 200, 255)) == 1
    # Förväntat resultat: Funktionen bör returnera 1 eftersom pixeln precis ligger vid den övre gränsen för himmelfärg.

    # Testfall 6: Testa en pixel som ligger precis vid den nedre gränsen för himmelfärg
    assert pixel_constraint(100, 150, 50, 200, 100, 255)((100, 50, 100)) == 1
    # Förväntat resultat: Funktionen bör returnera 1 eftersom pixeln precis ligger vid den nedre gränsen för himmelfärg.

test_pixel_constraint()
"""
Testfall 1 och 2 täcker de vanligaste fallen där pixeln antingen ligger inom eller utanför det angivna färgintervallet.
Testfall 3 och 4 är gränsfall där pixeln har ogiltig färg (None eller felaktigt index) och förväntas returnera None.
Testfall 5 och 6 testar extremvärden där pixeln ligger precis vid de övre respektive nedre gränserna för himmelfärg.

"""
def test_generator_from_image():
    # Testfall 1: Testa en generator för en lista med tre bilder
    image_list = ['image1.jpg', 'image2.jpg', 'image3.jpg']
    generator = generator_from_image(image_list)
    assert generator(0) == 'image1.jpg'
    assert generator(1) == 'image2.jpg'
    assert generator(2) == 'image3.jpg'
    # Förväntat resultat: Generatorn bör returnera rätt bild för varje index i bildlistan.

    # Testfall 2: Testa en generator för en tom bildlista
    empty_list = []
    empty_generator = generator_from_image(empty_list)
    assert empty_generator(0) == None
    # Förväntat resultat: Generatorn bör returnera None eftersom det inte finns några bilder i listan.

test_generator_from_image()

"""
Testfall 1 täcker det vanliga fallet där generatorn skapas från en lista med bilder och förväntas returnera rätt bild baserat på index.
Testfall 2 är ett extremfall där bildlistan är tom och förväntas resultera i att generatorn returnerar None.

"""
def test_combine_images():
    # Testfall 1: Testa att kombinera bilder med condition 1 (generator1 ska användas)
    image_list = [1, 2, 3, 4, 5]
    condition = lambda x: x == 1
    generator1 = lambda x: x * 10
    generator2 = lambda x: x * 100
    result = combine_images(image_list, condition, generator1, generator2)
    assert result == [10, 2, 3, 4, 5]
    # Förväntat resultat: Generator1 bör användas för pixeln med värdet 1 och generator2 för de andra pixlarna.

    # Testfall 2: Testa att kombinera bilder med condition 0 (generator2 ska användas)
    condition = lambda x: x == 0
    result = combine_images(image_list, condition, generator1, generator2)
    assert result == [100, 2, 3, 4, 5]
    # Förväntat resultat: Generator2 bör användas för pixeln med värdet 0 och generator1 för de andra pixlarna.

    # Testfall 3: Testa att kombinera bilder med condition baserat på index
    condition = lambda x: x % 2 == 0
    result = combine_images(image_list, condition, generator1, generator2)
    assert result == [10, 200, 30, 400, 50]
    # Förväntat resultat: Generator1 ska användas för pixlarna med jämna index och generator2 för de ojämna pixlarna.

test_combine_images()
"""
Testfall 1 och 2 täcker kombinationen av bilder med olika conditions där antingen generator1 eller generator2 ska användas beroende på condition.
Testfall 3 testar att kombinera bilder baserat på index där generator1 används för jämna index och generator2 för ojämna index.

"""