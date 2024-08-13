import cv2
import pytesseract

img = cv2.imread("teste.png")

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"
config = r'--oem 3 --psm 6'
resultado = pytesseract.image_to_string(img, config=config)

print (resultado)