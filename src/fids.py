from scaner import Scanner
from hids_file import HidsFile
from config.config import Config
from db_connector.db import Database


class FIDS:
    def scan_system(self):
        config = Config()
        scanner = Scanner(fids_config=config.fids_config)
        files = scanner.scan()
        print(files)
        db = Database(config.db_config)
        for file in files:
            db.safeFile(file)
        db.commit()


if __name__ == "__main__":
    FIDS().scan_system()
