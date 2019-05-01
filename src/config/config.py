import yaml
from .fids_config import FidsConfig
from .db_config import DbConfig


class Config:
    def __init__(self, config_file='./src/config.yaml'):
        with open(config_file, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        print(cfg)
        self.fids_config = FidsConfig(cfg['fids'])
        self.db_config = DbConfig(cfg['db'])
