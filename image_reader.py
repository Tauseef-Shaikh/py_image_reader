import cv2
import easyocr

reader = easyocr.Reader(['en'])
image_path = 'path/to/your/image.jpg'
img = cv2.imread(image_path)
results = reader.readtext(img)

print (results)