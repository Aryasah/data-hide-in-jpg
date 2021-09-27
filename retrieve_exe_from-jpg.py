with open('london.jpg','rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))

    f.seek(offset+2)
    with open('new_retrieved.exe','wb') as e:
        e.write(f.read())