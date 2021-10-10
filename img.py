import cv2


# c = r'assets/loli-cha.jpg'

print('Hello')

img = cv2.imread('assets/loli-chan.jpg', -1)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Imagem', img)
# cv2.imwrite('Copy_loli.jpg', img)
cv2.waitKey(0)

cv2.destroyAllWindows()


