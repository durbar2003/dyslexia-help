import sys

from PIL import Image
import pytesseract
import numpy as np
from cv2 import GaussianBlur, normalize, NORM_MINMAX, threshold, THRESH_BINARY
from spellchecker import SpellChecker
from autocorrect import Speller

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def readerMain(filename):

    spell = SpellChecker()
    spell2 = Speller(lang = "en")

    img = np.array(Image.open(filename))
    norm_img = np.zeros((img.shape[0], img.shape[1]))

    img = normalize(img, norm_img, 0, 255, NORM_MINMAX)
    img = threshold(img, 100, 255, THRESH_BINARY)[1]
    img = GaussianBlur(img, (1, 1), 0)

    def convert(lst):
        return ([i for item in lst for i in item.split()])

    text = [str(pytesseract.image_to_string(img))]
    ctext = convert(text)
    scheckedtext = []

    with open("Words.txt", "w+") as file:
        for i in ctext:
            i = spell2(spell.correction(i))
            scheckedtext.append(i)
            file.write(i + "\n")

    for i in range(7):
        scheckedtext.insert(0, "  ")

    return 