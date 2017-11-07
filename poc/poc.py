import cv2
import numpy as np
import pytesseract
import ocr
# open image:
img = cv2.imread('novo_assinar.jpg')

ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY), 150, 255, cv2.THRESH_BINARY_INV)
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
dilated = cv2.dilate(thresh, kernel, iterations=0)
# image, contours, hier = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

font = cv2.FONT_HERSHEY_SIMPLEX


teste = ocr.ocr_ocr()

tamanho = int(teste.__len__())

i = 0
while i < tamanho:
    print(teste[i])
    i += 1

# template image1
template = cv2.imread('NMar.jpg', 0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(dilated, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(dilated, pt, (pt[0] + w, pt[1] + h), (255, 255, 255), -2)
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 3)
    # cv2.putText(img,"  AUSENTE",(pt[0], pt[1]+45), cv2.FONT_HERSHEY_DUPLEX, 2, 255)
    cv2.putText(img, '  AUSENTE', (pt[0], pt[1] + 45), font, 2, (0, 0, 255), 3, cv2.LINE_AA)



# template image2
template2 = cv2.imread('Mar.jpg', 0)
w2, h2 = template2.shape[::-1]
res2 = cv2.matchTemplate(dilated, template2, cv2.TM_CCOEFF_NORMED)
threshold2 = 0.8
loc2 = np.where(res2 >= threshold2)
for pt2 in zip(*loc2[::-1]):
    cv2.rectangle(dilated, pt2, (pt2[0] + w2, pt2[1] + h2), (255, 255, 255), -2)
    cv2.rectangle(img, pt2, (pt2[0] + w2, pt2[1] + h2), (0, 255, 0), 3)
    cv2.putText(img, "   PRESENTE", (pt2[0], pt2[1] + 45), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
# cv2.putText(img,'  	 PRESENTE',(pt2[0], pt2[1]+45), font, 2,(0,255,0),2,cv2.LINE_AA)

# template image3
template3 = cv2.imread('1.jpg', 0)
w3, h3 = template3.shape[::-1]
res3 = cv2.matchTemplate(dilated, template3, cv2.TM_CCOEFF_NORMED)
threshold3 = 0.8
loc3 = np.where(res3 >= threshold3)
for pt3 in zip(*loc3[::-1]):
    cv2.rectangle(dilated, pt3, (pt3[0] + w3, pt3[1] + h3), (255, 255, 255), -2)
    cv2.rectangle(img, pt3, (pt3[0] + w3, pt3[1] + h3), (0, 255, 0), 1)
    cv2.putText(img, "   PRESENTE", (pt3[0], pt3[1] + 45), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
# cv2.putText(img,'   PRESENTE',(pt3[0], pt3[1]+45), font, 2,(0,255,0),2,cv2.LINE_AA)

# template image4
template4 = cv2.imread('2.jpg', 0)
w4, h4 = template4.shape[::-1]
res4 = cv2.matchTemplate(dilated, template4, cv2.TM_CCOEFF_NORMED)
threshold4 = 0.8
loc4 = np.where(res4 >= threshold4)
for pt4 in zip(*loc4[::-1]):
    cv2.rectangle(dilated, pt4, (pt4[0] + w4, pt4[1] + h4), (255, 255, 255), -2)
    cv2.rectangle(img, pt4, (pt4[0] + w4, pt4[1] + h4), (0, 255, 0), 3)
    cv2.putText(img, "   PRESENTE", (pt4[0], pt4[1] + 45), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
# cv2.putText(img,'   PRESENTE',(pt4[0], pt4[1]+45), font, 2,(0,255,0),2,cv2.LINE_AA)


# cv2.imshow("contours", img)
cv2.imwrite("contour.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
