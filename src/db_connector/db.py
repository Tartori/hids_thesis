import sqlite3
import os.path


class Database:
    def __init__(self, db_config):
        filepath = 'src/fids_db.db'
        needs_init = False
        if not os.path.exists(filepath):
            needs_init = True
        self.conn = sqlite3.connect(filepath)
        self.cursor = self.conn.cursor()
        if needs_init:
            self.setup()

    def setup(self):
        self.cursor.execute(
            ("CREATE TABLE FIDS_FILES("
                "path text, "
                "name text, "
                "file_type int, "
                "size int, "
                "mode int, "
                "creation_time int, "
                "modification_time int, "
                "access_time int, "
                "changed_time int);"))

    def safeFile(self, file):
        self.cursor.execute(
            "INSERT INTO FIDS_FILES(path, name, file_type, size, mode, creation_time, modification_time, access_time, changed_time) values (?,?,?,?,?,?,?,?,?); ",
            (file.path,
             file.name,
             int(file.file_type),
             file.size,
             file.mode,
             file.creation_time,
             file.modification_time,
             file.access_time,
             file.changed_time))

    def commit(self):
        self.conn.commit()
