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
            ("CREATE TABLE FIDS_RUN("
                "id text, "
                "config_hash text, "
                "start_time int, "
                "finish_time int);"))

        self.cursor.execute(
            ("CREATE TABLE FIDS_FILE("
                "run_id text,"
                "path text, "
                "name text, "
                "file_type int, "
                "size int, "
                "mode int, "
                "creation_time int, "
                "modification_time int, "
                "access_time int, "
                "changed_time int);"))

    def start_run(self, run):
        self.cursor.execute(
            "INSERT INTO FIDS_RUN(id, config_hash, start_time) values (?,?,?); ",
            (run.id,
             run.config_hash,
             run.start_time,
             ))

    def finish_run(self, run):
        self.cursor.execute(
            "UPDATE FIDS_RUN SET finish_time = ? WHERE id = ?; ",
            (run.finish_time,
             run.id,
             ))

    def safe_file(self, file, run):
        self.cursor.execute(
            "INSERT INTO FIDS_FILE(run_id, path, name, file_type, size, mode, creation_time, modification_time, access_time, changed_time) values (?,?,?,?,?,?,?,?,?,?); ",
            (run.id,
                file.path,
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
