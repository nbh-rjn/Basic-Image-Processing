from PIL import Image

def FlipImg(img, flag=0):
    if flag == 0:
        flipped_image = img.transpose(Image.FLIP_LEFT_RIGHT)
    else:
        flipped_image = img.transpose(Image.FLIP_TOP_BOTTOM)

    flipped_image.save("task4.png")


input_image = Image.open("image2.png")
#FlipImg(input_image, flag=1)
FlipImg(input_image, flag=0)

