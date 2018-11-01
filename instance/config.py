import os


class Configurations():
    DEBUG = False
    TESTING = False
    DBNAME = os.getenv('DBNAME')
    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT') 
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    DBURL = os.getenv('DEVELOPMENT_URL')


class Development(Configurations):
    DEBUG = True
    DBNAME = os.getenv('DBNAME')
    DBURL = os.getenv('DEVELOPMENT_URL')


class Testing(Configurations):
    DEBUG = True
    TESTING = True
    # DBNAME = 'teststoremanagerdb'
    # DBURL = os.getenv('TESTING_URL')


class Production(Configurations):
    DEBUG = False
    TESTING = False


app_configurations = {
    "development": Development,
    "testing": Testing,
    "production": Production
}
