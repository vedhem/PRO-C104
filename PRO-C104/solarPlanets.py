import cv2

img = cv2.imread('solar-system.jpg')
cv2.imshow('output', img)
cv2.waitKey(0)

cv2.putText(img, "sun", (20, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale = 0.5, color = (225, 225, 255))
cv2.putText(img, "mercury", (40, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale = 0.5, color = (225, 225, 255))
cv2.putText(img, "venus", (60, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale = 0.5, color = (225, 225, 255))
cv2.putText(img, "earth", (80, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale = 0.5, color = (225, 225, 255))
cv2.putText(img, "mars", (100, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale = 0.5, color = (225, 225, 255))
cv2.putText(img, "jupiter", (120, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale = 0.5, color = (225, 225, 255))
cv2.putText(img, "saturn", (140, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale = 0.5, color = (225, 225, 255))
cv2.putText(img, "uranus", (160, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale = 0.5, color = (225, 225, 255))
cv2.putText(img, "neptune", (180, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale = 0.5, color = (225, 225, 255))


