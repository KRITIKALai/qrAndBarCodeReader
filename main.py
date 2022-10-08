import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('QRcodes\\qr1.png')
code = decode(img)
print(code)