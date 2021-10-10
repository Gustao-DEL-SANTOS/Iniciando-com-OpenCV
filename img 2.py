import cv2


# c = r'assets/loli-cha.jpg'

img = cv2.imread('assets/loli-chan.jpg', -1)
# r,g,b = 0, 0, 0
# for i in range(400):
#     if i%2 == 0:
#         b += 10
#         for j in range(img.shape[1]):
#             img[i][j] = [b, g, r]
#     else:
#         r += 15
#         g += 20

tag = img[0:400, 0:400]
img[0:400, 0:400] = tag

print(img)

cv2.imshow('Imagem', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


