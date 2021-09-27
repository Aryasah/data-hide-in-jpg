import PIL.Image
import io

with open("london.jpg",'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))

    f.seek(offset+2) #GOING TO THE POSITION WHERE NEW FILE IS ADDED 

    retrieved_img = PIL.Image.open(io.BytesIO(f.read())) #READING BYTES STREAM FROM THERE

    retrieved_img.save("retrieval_png_from_jpg.png") #saving deleted image