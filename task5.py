from PIL import Image


def CommonImg(img1, img2):
    if img1.size != img2.size:
        raise ValueError("Images must have the same dimensions")

    result_image = Image.new("RGB", img1.size, color=(0, 0, 0))

    pixels1 = img1.load()
    pixels2 = img2.load()
    result_pixels = result_image.load()

    for y in range(img1.size[1]):
        for x in range(img1.size[0]):
            if pixels1[x, y] == pixels2[x, y]:
                result_pixels[x, y] = (0, 255, 255)

    result_image.save("task5.png")


image1 = Image.open("img1.png").convert("L")
image2 = Image.open("img2.png").convert("L")
CommonImg(image1, image2)
