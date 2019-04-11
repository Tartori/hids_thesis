import pytsk3
img_info = pytsk3.Img_Info("/dev/nvme0n1p5")
print(img_info)
fs_info = pytsk3.FS_Info(img_info, offset=0)
print(fs_info.info)
fs_info.info

root = fs_info.open_dir("/")
for i in root:
    print(i.info.name.name)
    print(i.info.name.type)
    if i.info.name.type==pytsk3.TSK_FS_NAME_TYPE_DIR:
        print("directory!")
    elif i.info.name.type == pytsk3.TSK_FS_NAME_TYPE_REG:
        print("I'm a file")
        curDir = i.open_dir()
        for j in curDir:
                print(j.info.name.name)
                print(j.info.name.type)



def open_directory_rec(path):
        curDir = fs_info.open_dir(path)
        for element in curDir:
                print(path)
                print(element.info.name.name)
                print(element.info.name.type)
                if element.info.name.type==pytsk3.TSK_FS_NAME_TYPE_DIR:
                        print("directory!")
                        if(not element.info.name.name==b'.' and not element.info.name.name==b'..'):
                                print("valid directory")
                                open_directory_rec(path + element.info.name.name.decode("ascii") + "/")
                elif element.info.name.type == pytsk3.TSK_FS_NAME_TYPE_REG:
                        print("I'm a file")

