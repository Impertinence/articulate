import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
	print('cannot open camera')#
while True:
	ret, frame = cap.read()

	if not ret:
		print('asd')

	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

	cv.imshow('frame', gray)
	if cv.waitKey(1) == ord('q'):
		breakasd

cap.release()
cv.destroyAllWindows()
