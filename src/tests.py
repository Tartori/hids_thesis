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
        if element.info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
            print("directory!")
            if(not element.info.name.name == b'.' and not element.info.name.name == b'..'):
                print("valid directory")
                open_directory_rec(
                    path + element.info.name.name.decode("ascii") + "/")
        elif element.info.name.type == pytsk3.TSK_FS_NAME_TYPE_REG:
            print("I'm a file")


img_file_path = '/dev/nvme0n1p5'
# img_file_path = '../images/usb1.dd'
path = '/home/julian/school/hids_thesis/src/'
# path='/'
img_info = pytsk3.Img_Info(img_file_path)
fs_info = pytsk3.FS_Info(img_info, offset=0)
fs_info.info

curDir = fs_info.open_dir(path)

tsk_file = curDir.__next__()
tsk_file.name.name
tsk_file = curDir.__next__()
tsk_file = curDir.__next__()

open_directory_rec(path)

pytsk3.TSK_FS_META_MODE_IRUSR.__str__()
pytsk3.TSK_FS_META_MODE_IRGRP.__str__()
pytsk3.TSK_FS_META_MODE_IROTH.__str__()
pytsk3.TSK_FS_META_MODE_IWUSR.__str__()
pytsk3.TSK_FS_META_MODE_IWGRP.__str__()
pytsk3.TSK_FS_META_MODE_IWOTH.__str__()
pytsk3.TSK_FS_META_MODE_IXUSR.__str__()
pytsk3.TSK_FS_META_MODE_IXGRP.__str__()
pytsk3.TSK_FS_META_MODE_IXOTH.__str__()


print("Attribute %s, type %s, id %s" %
      (at.info.name, at.info.type, at.info.id))


for attr in f:
    print("Attribute %s, type %s, id %s" % (attr.info.name,
                                            attr.info.type,
                                            attr.info.id))
    for run in attr:
        print("   Blocks %s to %s (%s blocks)" %
              (run.addr, run.addr + run.len, run.len))
