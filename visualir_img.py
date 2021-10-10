import cv2 as cv


link = 'assets/teste_luz.jpg'
link2 = 'assets/teste_luz.jpg'
img = cv.imread(link, 0)
img2 = cv.imread(link2, 0)
img2 = cv.resize(img2, (0, 0), fx=0.5, fy=0.5)
tg = img2[0: img.shape[0], 0: img.shape[1]]

# img[0: , 0: ][0: , 0: ] = img * tg
img += -img*2
cv.imshow('Image', img)


cv.waitKey(0)
cv.destroyAllWindows()

