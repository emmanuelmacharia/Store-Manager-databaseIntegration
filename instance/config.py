import os

class Configurations():
    DEBUG = False
    TESTING = False

# parameters = {
#     "dbname":os.getenv("storemanager"),
#     "host":os.getenv("localhost"),
#     "port":os.getenv(5432),
#     "user":os.getenv("postgres"),
#     "password":os.getenv("Permafrost")
# }
#{}"dbname='storemanager' host='localhost' port=5432 user='postgres' password='Permafrost'"

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
