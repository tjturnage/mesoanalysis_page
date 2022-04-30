print('hello!')
dest = open('C:/data/desc.txt', 'w')
with open('C:/data/PAH_MESO_Remote_V2.txt', 'r', encoding='utf-8-sig') as src:
    dat = src.readlines()
    for d in dat:
        if 'title' in d and 'onfocus' in d:
            print(d)
            dest.write(d)

dest.close()