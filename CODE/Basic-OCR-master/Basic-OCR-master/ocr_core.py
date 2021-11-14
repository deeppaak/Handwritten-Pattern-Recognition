try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
# import keras


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)
    # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    text = pytesseract.image_to_string(gray, lang='eng')
    print(text, 'fun')
    return text  # Then we will print the text in the image


# model = kedras.models.load_model('./model.hdf5')


def ocr_core1(filename):
    """
    This function will handle the core OCR processing of images.
    """
    a = list('ABCDEFGHIJKLMONPQRSTUVWXYZ')
    img = cv2.imread(filename)

    text = pytesseract.image_to_string(imgim, lang='eng')
    print(text, 'fun')
    return text  # Then we will print the text in the image
