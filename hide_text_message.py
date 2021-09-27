# Opening file.jpg in append mode by writing 'ab'
with open("london.jpg",'ab') as f:
    f.write(b"Your String Here That is to be send in image")

    # using b because we are writing bytestream



