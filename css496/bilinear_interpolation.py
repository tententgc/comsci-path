from PIL import Image

def bilinear_resize(image, width, height):

    original_width, original_height = image.size
    resized_image = Image.new("RGB", (width, height))
    pixels = resized_image.load()
    
    for i in range(width):
        for j in range(height):
            x = i * (original_width - 1) / (width - 1)
            y = j * (original_height - 1) / (height - 1)
            
            x0, y0 = int(x), int(y)
            x1, y1 = min(x0 + 1, original_width - 1), min(y0 + 1, original_height - 1)
            
            f00 = image.getpixel((x0, y0))
            f10 = image.getpixel((x1, y0))
            f01 = image.getpixel((x0, y1))
            f11 = image.getpixel((x1, y1))
            
            px = x - x0
            py = y - y0
            
            red = (f00[0] * (1 - px) + f10[0] * px) * (1 - py) + (f01[0] * (1 - px) + f11[0] * px) * py
            green = (f00[1] * (1 - px) + f10[1] * px) * (1 - py) + (f01[1] * (1 - px) + f11[1] * px) * py
            blue = (f00[2] * (1 - px) + f10[2] * px) * (1 - py) + (f01[2] * (1 - px) + f11[2] * px) * py
            
            pixels[i, j] = (int(red), int(green), int(blue))
            
    return resized_image


image = Image.open("tenten.jpeg")
resized_image = bilinear_resize(image, 325, 325)
resized_image.save("Bilinear_resized.jpg")
