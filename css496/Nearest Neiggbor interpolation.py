import cv2
import numpy as np

def show_difference(image_path, fx=0.5, fy=0.5):
    original_image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if original_image is None:
        print("Error loading image!")
        return

    resized_image = cv2.resize(original_image, (256,256), fx=fx, fy=fy, interpolation=cv2.INTER_NEAREST)

    cv2.imshow("original_image", original_image) 
    cv2.imshow("resized_image", resized_image) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = 'tenten.jpeg'
show_difference(image_path)
