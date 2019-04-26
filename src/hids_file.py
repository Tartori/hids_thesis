import pytsk3


class HidsFile:
    def __init__(
            self,
            path="",
            name="",
            file_type="",
            size=0,
            creation_time=0,
            modification_time=0,
            access_time=0,
            changed_time=0,
            mode=0,
    ):
        self.path = path
        self.name = name
        self.file_type = file_type
        self.size = size
        self.mode = mode
        self.creation_time = creation_time
        self.modification_time = modification_time
        self.access_time = access_time
        self.changed_time = changed_time

    def set_path(self, path):
        self.path = path

    def parse_tsk_file(self, tsk_file):
        """ return void
            will parse a TSK_FS_FILE in the structure defined here.
            The TSK API Documentation can be found here 
            <http://www.sleuthkit.org/sleuthkit/docs/api-docs/4.5/structTSK__FS__FILE.html>
            Be sure to set the path either in the constructor or with the set_path function.
        """
        self.name = tsk_file.info.name.name.decode("ascii")
        self.file_type = int(tsk_file.info.name.type)
        self.size = tsk_file.info.meta.size  # size in bytes
        self.creation_time = tsk_file.info.meta.crtime
        self.modification_time = tsk_file.info.meta.mtime
        self.access_time = tsk_file.info.meta.atime
        self.changed_time = tsk_file.info.meta.ctime
        self.mode = int(tsk_file.info.meta.mode)

    def __repr__(self):
        return ('HidsFile('
                f'path="{self.path}",'
                f'name="{self.name}",'
                f'file_type="{self.file_type}",'
                f'size={self.size},'
                f'creation_time={self.creation_time},'
                f'modification_time={self.modification_time},'
                f'access_time={self.access_time},'
                f'changed_time={self.changed_time},'
                f'mode={self.mode},)')


# pytsk3.TSK_FS_META_MODE_IRUSR.__str__()
# pytsk3.TSK_FS_META_MODE_IRGRP.__str__()
# pytsk3.TSK_FS_META_MODE_IROTH.__str__()
# pytsk3.TSK_FS_META_MODE_IWUSR.__str__()
# pytsk3.TSK_FS_META_MODE_IWGRP.__str__()
# pytsk3.TSK_FS_META_MODE_IWOTH.__str__()
# pytsk3.TSK_FS_META_MODE_IXUSR.__str__()
# pytsk3.TSK_FS_META_MODE_IXGRP.__str__()
# pytsk3.TSK_FS_META_MODE_IXOTH.__str__()
# path
# tsk_file.info.name.type
