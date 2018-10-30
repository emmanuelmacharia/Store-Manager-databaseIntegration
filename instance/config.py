import os

class Configurations():
    DEBUG = False
    TESTING = False
    DBNAME= os.getenv('DBNAME')
    HOST= os.getenv('HOST')
    PORT=os.getenv('PORT') 
    USER=os.getenv('USER')
    PASSWORD=os.getenv('PASSWORD')

class Development(Configurations):
    DEBUG = True

class Testing(Configurations):
    DEBUG = True
    TESTING = True
    DBNAME = 'teststoremanagerdb'

class Production(Configurations):
    DEBUG = False
    TESTING = False


app_configurations= {
    "development": Development,
    "testing": Testing,
    "production": Production
}
