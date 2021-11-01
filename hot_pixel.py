import cv2

print("###------ PROJECT-CMOS-COOLING :@@@ Hot Pixel Number @@@ -------###\n")
choix = ""
n = 1

while  choix != "end.jpg":

    choix = str(input("Name image: ")+".jpg")
    gray = cv2.imread(choix, 0)

## threshold : Si la valeur du pixel est supérieure à une valeur seuil,
#une valeur lui est attribuée (peut être blanche), sinon une autre
#valeur lui est attribuée (peut être noire).
#La fonction utilisée est cv2.threshold

    th, threshed = cv2.threshold(gray, 100, 255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

## findcontours : utilisation de la fonction cv2.findContours()
#pour détecter les objets dans une image
    cnts = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]


#comparaison de la valeur du pixel aux valeurs seuil,
#Si la valeur du pixel est supérieure à une valeur seuil,
#une valeur lui est attribuée (peut être blanche), sinon une autre
#valeur lui est attribuée (peut être noire)
    seuil_1 = 1
    seuil_2 = 15
    xcnts = []
    
    for cnt in cnts:
        if seuil_1 < cv2.contourArea(cnt) < seuil_2:
            xcnts.append(cnt)
    print("Hot pixel number for image"+str(n)+": {}\n".format(len(xcnts)))

    n += 1
