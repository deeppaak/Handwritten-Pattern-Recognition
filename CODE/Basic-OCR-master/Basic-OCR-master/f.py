import pytesseract
from PIL import Image


def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(
        filename))
    print(text, 'fun')
    return text


ocr_core('./static/uploads/logo-ENGLISH.png')
