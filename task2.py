from PIL import Image


image = Image.open("image.png")
image = image.convert("RGB")
image = image.convert("L", matrix=(0.299, 0.587, 0.114, 0))
image.save("task2.png")
