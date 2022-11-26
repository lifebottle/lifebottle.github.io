from PIL import Image
import os
 
print("Shrink images in the folder")
folder = r"..\..\projects\destiny-dc\leon-guide"
w = int('640')
h = int('480')
for i in os.listdir(folder):
    file = f"{folder}\\{i}"
    im = Image.open(file)
    im = im.resize((w, h), Image.ANTIALIAS)
    im.save(file,quality=20,optimize=True) # change 'file' to something else to avoid overwriting image in the same folder