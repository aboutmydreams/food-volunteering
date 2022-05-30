def write_json():
    with open('名单.txt','r') as f:
        f_line = f.readlines()
    class_zip = {}
    for i in f_line:
        ban_site = i.find('班')
        ban = i[:ban_site+1]
        name = i[ban_site+1:].replace('\n','')
        print(name)
        class_zip[name] = f'{ban}'
    with open('ban.json','w') as f0:
        f0.write(str(class_zip))

def read_json():
    with open('ban.json','r') as f:
        rf = f.read()
    return rf

def set_root():
    with open('root.txt','w') as f:
        f.write('spxyzqs:::lsl2016')
