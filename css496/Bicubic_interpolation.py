from PIL import Image

def resize_image_with_bicubic(input_path, output_path, target_width, target_height):
    with Image.open(input_path) as img:
        resized_img = img.resize((target_width, target_height), Image.BICUBIC)
        resized_img.save(output_path)


resize_image_with_bicubic('tenten.jpeg', 'bicubic.jpg', 300, 300)
