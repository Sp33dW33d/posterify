from PIL import Image, ImageOps
from pathlib import Path

def counter(start = 1) -> GeneratorExit:
    n = start
    while True:
        yield n
        n += 1

def load_image(image_path: Path) -> Image:
    return Image.open(image_path)

def pad_image(image: Image, padding: tuple, color: int) -> Image:
    return ImageOps.expand(img, border = padding, fill = color)

def crop_image(image: Image, box: tuple) -> Image:
    return image.crop(image, box) 

def generate_tiles() -> tuple[Image]:
    ...

def save_tiles(tiles: tuple, num: int) -> None:
    for tile in tiles:
        tile.save(f"tile_{num:03d}.jpg")

def generate_pdf(images: tuple[Image], output_path: Path) -> None:
    images[0].save(
        output_path,
        save_all = True,
        append_images=images[1:]
    )

if __name__ == "__main__":
    IMG_PATH = Path("D:\Coding_Stuff\Codes\Python\posterify\WhatsApp Image 2025-08-31 at 6.10.45 PM.jpeg")
    img = load_image(IMG_PATH)
    print(img.format, img.size)
    # img.show()
    box = (0,0,100,64)

    # padded_image = pad_image(img, (700,234), color = "#FF0000")
    pad_x = img.size[0] + 100
    pad_y = img.size[1] + 100

    padded_image = pad_image(img, (0,0,100,100), "#FF0000")
    padded_image.show()

    print(padded_image.format, padded_image.size)
