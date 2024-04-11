from PIL import Image


image = Image.open("image.png")
image = image.convert("RGBA")

width, height = image.size
pixels = image.load()

for y in range(height):
    for x in range(width):
        pixel = pixels[x, y]
        if pixel[:3] <= (81, 81, 81):
            pixels[x, y] = (0, 0, 0, 0)

image.save("task1.png")
