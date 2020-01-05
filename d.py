import os
import cv2
import matplotlib.pyplot as plt
from imageai.Detection import ObjectDetection
import matplotlib.image as mpimg




cap = cv2.VideoCapture(0)
a=0
while True:
	a = a+1
	#create frame object
	check, frame= cap.read()

	print(check)
	print(frame)#representing frame
	#change color to gray
	#gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	#show the frame
	cv2.imshow("capturing", frame) 

	#for press any key to out melliseconds
	#cv2.waitKey(0)

	#for video playing
	key = cv2.waitKey(1)
	if key == ord('q'):
		img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

		plt.imshow(img1)
		plt.title("Cemara Image-1")
		plt.xticks([])
		plt.yticks([])
		plt.show()
		mpimg.imsave("image.jpg", img1)
		break

print("total captures:", a)
cap.release() 
cv2.destroyAllWindows()

 