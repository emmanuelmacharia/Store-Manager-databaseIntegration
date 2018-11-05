import os


class Configurations():
    DEBUG = False
    TESTING = False
    DBNAME = os.getenv('DBNAME')
    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    DATABASE_URI = os.getenv('DATABASE_URI')


class Development(Configurations):
    '''development environment'''
    DEBUG = True


class Testing(Configurations):
    '''testing environment'''
    DEBUG = True
    TESTING = True
    DATABASE_URI = os.getenv('TESTDATABASE_URI') 


# class Production(Configurations):
#     '''production environment'''
#     DEBUG = False
#     TESTING = False


app_configurations = {
    "development": Development,
    "testing": Testing,
    # "production": Production
}
