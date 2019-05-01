import pytsk3
from hids_file import HidsFile


class Scanner:

    def __init__(self, image_path="/dev/nvme0n1p5", path="/home/julian/school/hids_thesis/src"):
        self.img_path = image_path
        self.path = path

    def scan(self):
        self.files = []
        img_info = pytsk3.Img_Info(self.img_path)
        fs_info = pytsk3.FS_Info(img_info, offset=0)
        fs_info.info
        self.open_directory_rec(self.path)
        return self.files

    def open_directory_rec(self, path):
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
                    self.open_directory_rec(
                        path + element.info.name.name.decode("ascii") + "/")
            elif element.info.name.type == pytsk3.TSK_FS_NAME_TYPE_REG:
                print("I'm a file")
                hids_file = HidsFile(path=path)
                hids_file.parse_tsk_file(element)
                self.files.append(hids_file)


if __name__ == "__main__":
    from pprint import pprint
    scanner = Scanner(path="/", image_path="../images/usb1.dd")
    pprint(scanner.scan())
