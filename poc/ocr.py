import cv2
import numpy as np
import pytesseract
import unicodedata
from PIL import Image

def ocr_ocr():
    # Abre arquivo de saida .txt
    saida = open("presenca.txt", 'a')

    # Abre a image para leitura
    img = cv2.imread('novo_assinar.jpg')

    ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    cv2.imwrite("contour11.jpg", thresh1)

    im = Image.open("contour11.jpg")
    # Aplica o OCR
    text = pytesseract.image_to_string(im)

    # Convertendo unicode para string
    convert_text = unicodedata.normalize('NFKD', text).encode('ascii','ignore')

    # Coloca o conteudo em uma lista
    conteudo = []
    for line in convert_text.splitlines():
        conteudo.append(line)

    for element in conteudo:
        if element == 'OOOOOOO':
            conteudo.remove(element)

    for element in conteudo:
        if element == ' ':
            conteudo.remove(element)

    for i in range(10):
        for element in conteudo:
            if element == '':
                conteudo.remove(element)
    ii = 10
    nconteudo = []
    while ii < conteudo.__len__():
        nconteudo.append(conteudo[ii])
        ii += 1

    # Fecha o arquivo de saida
    saida.close()

    return nconteudo

if (__name__ == "__main__"):
    ocr_ocr()