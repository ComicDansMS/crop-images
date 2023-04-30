# Image Autocrop

This script automatically crops images to remove unnecessary background space and focuses on the primary object in the given image. It works with both transparent (PNG) and non-transparent images (JPEG, BMP, GIF, TIFF, and WebP).

## Requirements

- Python 3.7+
- Pillow library: `pip install pillow`
- tqdm library: `pip install tqdm`

## Usage

1. Place the input images you want to process in the `images` folder.
2. Run the script with the following command: `python crop.py`.
3. The processed images will be saved in the `processed` folder.

## Configuration

You can adjust the following parameters in the `crop.py` script as needed:

- `alpha_threshold`: Changes the minimum alpha value to consider a pixel as part of the object in transparent images (default is 50).
- `color_difference_threshold`: Changes the minimum color difference parameter to consider a pixel as part of the object in non-transparent images (default is 50).