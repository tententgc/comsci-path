import cv2

def add_text_to_image_opencv(input_image_path, output_image_path, text):
    image = cv2.imread(input_image_path)

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    color = (0, 0, 255)

    position = (40, 40)

    cv2.putText(image, text, position, font, font_scale, color, font_thickness, lineType=cv2.LINE_AA)

    cv2.imwrite(output_image_path, image)

input_path = "tenten.jpeg"
output_path = "modified_image.jpg"
text = "Name:Thanyapisit ID:64090500404"
add_text_to_image_opencv(input_path, output_path, text)
