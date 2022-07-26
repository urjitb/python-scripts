from PIL import Image
import os

print("Shrink images in the folder")
folder = input("folder: ")
pHRem = input("Height % to crop: ")
for i in os.listdir(folder):
    file = f"{folder}/{i}"
    im = Image.open(file)
    width, height = im.size
    im = im.crop((0, 0, width*(int(pHRem)/100), height*(int(pHRem)/100)))
    im.save(file)