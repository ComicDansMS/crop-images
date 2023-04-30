import os
from PIL import Image
from tqdm import tqdm

def find_bounding_box(image, alpha_threshold=50):
    pixels = image.load()
    min_x, min_y = image.size
    max_x = max_y = 0

    for x in range(image.width):
        for y in range(image.height):
            if pixels[x, y][3] >= alpha_threshold:
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)

    return (min_x, min_y, max_x, max_y)

def find_bounding_box_rgb(image, color_difference_threshold=50):
    bg_color = image.getpixel((0, 0))
    min_x, min_y = image.size
    max_x = max_y = 0

    for x in range(image.width):
        for y in range(image.height):
            pixel_color = image.getpixel((x, y))
            color_difference = sum(abs(bg_color[i] - pixel_color[i]) for i in range(3))

            if color_difference >= color_difference_threshold:
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)
    
    return (min_x, min_y, max_x, max_y)

def crop_image(image):
    if image.mode == "RGBA":
        bbox = find_bounding_box(image)
    else:
        bbox = find_bounding_box_rgb(image)
    return image.crop(bbox)

script_dir = os.path.dirname(os.path.abspath(__file__))

input_directory = os.path.join(script_dir, "images")
output_directory = os.path.join(script_dir, "processed")

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

image_extensions = [".bmp", ".gif", ".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp"]
image_files = [f for f in os.listdir(input_directory) if any(f.endswith(ext) for ext in image_extensions)]

with tqdm(total=len(image_files), desc="Processing images") as pbar:
    for filename in image_files:
        filepath = os.path.join(input_directory, filename)
        image = Image.open(filepath)
        cropped_image = crop_image(image)
        
        output_filepath = os.path.join(output_directory, filename)
        cropped_image.save(output_filepath)
        pbar.update(1)