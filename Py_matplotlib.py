from PIL import Image
im = Image.open("Solny.jpg")
print(im.format, im.size, im.mode)
##im.show()