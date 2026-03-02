from PIL import Image, ImageOps
from pathlib import Path

# a4 dimensions
# 210 * 297 mm
# 8.27 x 11.69 inches
# 2481 x 3507
# 300 dpi

def counter(start = 1) -> GeneratorExit:
    n = start
    while True:
        yield n
        n += 1

def load_image(image_path: Path) -> Image:
    return Image.open(image_path)

def pad_image(image: Image, padding: tuple, color: int) -> Image:
    return ImageOps.expand(img, border = padding, fill = color)

def rescale_img(image: Image, factor: float) -> Image:
    return ImageOps.scale(image, factor)

def crop_image(image: Image, box: tuple) -> Image:
    return image.crop(box) 

def generate_tiles(image: Image, ) -> tuple[Image]:
    tiles = []
    tiles.append(crop_image(image,box))

def save_tiles(tiles: tuple[Image], num: int) -> None:
    for tile in tiles:
        tile.save(f"tile_{num:03d}.jpg")

def generate_pdf(images: tuple[Image], output_path: Path) -> None:
    images[0].save(
        output_path,
        save_all = True,
        append_images=images[1:]
    )

def get_crop_frame() -> tuple:
    """decides the crop frame for the image"""
    raise NotImplementedError

def get_next_crop_frame(image_size: tuple) -> tuple:
    raise NotImplementedError
    
if __name__ == "__main__":
    IMG_PATH = Path("D:\Coding_Stuff\miku.png")
    DPI = 300
    img = load_image(IMG_PATH)

    # this is in inches
    required_width = 8.27 * 2
    # this is in pixels
    required_pixel_width = required_width * DPI 
    scaling_factor = required_pixel_width / img.width

    print(f"Current width: {img.width}px\tRequired width:{required_pixel_width}px")
    rescaled_img = rescale_img(img, scaling_factor)

    print(rescaled_img.width)
    # rescaled_img.show()

    # ---
    box = (0,0,2481,3507)
    tile_001 = crop_image(rescaled_img, box)
    tile_001.show()