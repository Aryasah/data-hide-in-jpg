import PIL.Image
import io

img = PIL.Image.open('photo.png')
byte_arr = io.BytesIO()
img.save(byte_arr,format='PNG')  #Copying data of png in byte array

with open('london.jpg','ab') as f:
    f.write(byte_arr.getvalue())