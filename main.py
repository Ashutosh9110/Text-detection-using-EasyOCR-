import pytesseract
from pytesseract import Output
import cv2

myconfig = r"--psm 11 --oem 3"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread("C:\\Users\\veni_\\Desktop\\Internship\\Resolute AI Software Private Limited\\Data\\Data\\Task2\\2.png")

height, width, _ = img.shape

data = pytesseract.image_to_data(img, config=myconfig, output_type= Output.DICT)
print(data["text"])

amount_boxes = len(data["text"])
for i in range(amount_boxes):
    if float(data["conf"][i]) > 20:
        (x, y, width, height) = (data["left"][i], data["top"][i], data["width"][i], data["height"][1])
        img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)
        img = cv2.putText(img, data["text"][i], (x, y + height + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow("img", img)
cv2.waitKey(0)
