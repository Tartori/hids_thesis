class FidsConfig:
    def __init__(self, config):
        self.image_path = config['image_path']
        self.scan_paths = config['scan_paths']
        self.ignore_paths = config['ignore_paths']
        self.validate_mode = config['validate_mode']
