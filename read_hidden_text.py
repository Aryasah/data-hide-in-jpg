#READING HIDDEN TEXT MESSAGE
with open("london.jpg",'rb') as f: #OPENING FILES IN READMODE 'RB' 
    content= f.read()
    offset = content.index(bytes.fromhex('FFD9'))   #SETTING OFFSET TO POSITION AT WHICH FFD9 IS FOUND WHICH IS HEXD DO NEED TO BE CONVERTED TO BYTES

    f.seek(offset + 2)
    print(f.read())
