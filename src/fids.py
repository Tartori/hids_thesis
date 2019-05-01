from scaner import Scanner
from hids_file import HidsFile


class FIDS:
    def scan_system(self):
        scanner = Scanner(image_path="../images/usb1.dd", path="/")
        files = scanner.scan()
        print(files)


if __name__ == "__main__":
    pass
