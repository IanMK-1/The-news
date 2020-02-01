class Config:
    """Parent configuration class"""
    pass


class ProdConfig(Config):
    """Configuration used during production. Inherits from parent class"""
    pass


class DevConfig(Config):
    """Configuration used during development stage"""

    DEBUG = True
