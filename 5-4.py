def file_search(folder, filename):
    adress = folder[0]
    if filename in folder:
        adress = adress + '/' + filename
        return adress
    for dir in folder:
        if type(dir) == type(['kj']):
            adress_2 = file_search(dir, filename)
            if adress_2 != False:
                adress = adress + '/' + adress_2
                break
    if adress == folder[0]:
        return False
    else:
        return adress