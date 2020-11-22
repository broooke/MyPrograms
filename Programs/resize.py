from PIL import Image

img = Image.open("2_1080x2160.1.png")
new_img = img.resize((400,800))
new_img.save("newphoti.png")
print(img.size)
print(new_img.size)