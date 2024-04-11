from PIL import Image


img1 = Image.open("image.png")
img2 = Image.open("image.png")

if img1.size != img2.size or img1.mode != img2.mode:
    raise ValueError("Images are not consistent")

width, height = img1.size

result = Image.new(img1.mode, (width * 2, height))

result.paste(img1, (0, 0))
result.paste(img2, (width, 0))

result.save("task3.png")
