import sys
import numpy as np
import pytesseract
from PIL import Image
from cv2 import GaussianBlur, normalize, NORM_MINMAX, THRESH_BINARY, threshold
from spellchecker import spellcheckerfrom autocorrect import spellchecker

