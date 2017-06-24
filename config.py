class Config:
    SECRET_KEY = 'anything'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://koko:owonikoko@127.0.0.1:5432/todolistdb'

class Production(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://koko:owonikoko@127.0.0.1:5432/todolistdb'
    DEBUG = False

class Testing(Config):
     SQLALCHEMY_DATABASE_URI = 'sqlite:///todolistdb.sqlite'

config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}
