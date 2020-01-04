#Built by Pranav Hegde and Articulate Machines
#Copyright 2020 Articulate Machines

import cv2
from Naked.toolshed.shell import execute_js, muterun_js

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:
	#while true capture video from standard webcam
	ret, frame = video_capture.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	#Detect faces
	def faceDetection():
		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(30, 30),
			flags=cv2.CASCADE_SCALE_IMAGE
		)

		num_faces = len(faces)
		if num_faces > 0:
			voice = execute_js('voice_test.js')

			if voice:
				print('success')
			else:
				print('err')

		for(x, y, w, h) in faces:
			cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)

	faceDetection()
	cv2.imshow('video', gray)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

video_capture.release()
cv2.destroyAllWindows()
