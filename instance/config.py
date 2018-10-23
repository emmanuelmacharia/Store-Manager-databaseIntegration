
import os



class Configurations():

    DEBUG = False

    TESTING = False



class Development(Configurations):

    DEBUG = True



class Testing(Configurations):

    DEBUG = True

    TESTING = True



class Production(Configurations):

    DEBUG = False

    TESTING = False



app_configurations= {

    "development": Development,

    "testing": Testing,

    "production": Production

}
