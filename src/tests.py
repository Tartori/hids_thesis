import pytsk3

def open_directory_rec(path):
        try:
                curDir = fs_info.open_dir(path)
        except:
                print("exception!")
                return
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

img_info = pytsk3.Img_Info("/dev/nvme0n1p5")
fs_info = pytsk3.FS_Info(img_info, offset=0)
fs_info.info

open_directory_rec("/home/")

pytsk3.TSK_FS_META_MODE_IRUSR.__str__()
pytsk3.TSK_FS_META_MODE_IRGRP.__str__()
pytsk3.TSK_FS_META_MODE_IROTH.__str__()
pytsk3.TSK_FS_META_MODE_IWUSR.__str__()
pytsk3.TSK_FS_META_MODE_IWGRP.__str__()
pytsk3.TSK_FS_META_MODE_IWOTH.__str__()
pytsk3.TSK_FS_META_MODE_IXUSR.__str__()
pytsk3.TSK_FS_META_MODE_IXGRP.__str__()
pytsk3.TSK_FS_META_MODE_IXOTH.__str__()