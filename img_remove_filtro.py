import cv2 as cv


link = 'assets/legion.jpg'

img = cv.imread(link, -1)

r, g, b = 1, 1, 1

for i in range(img.shape[0]):

    for j in range(img.shape[1]):
        img[i][j] = img[i][j]- img[i][j]*2-200


cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()

