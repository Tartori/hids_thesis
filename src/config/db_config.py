class DbConfig:
    def __init__(self, config):
        self.host = config['host']
        self.port = config['port']
        self.dbname = config['dbname']
        self.user = config['user']
        self.password = config['password']
