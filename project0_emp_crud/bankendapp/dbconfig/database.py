import pymysql
from django.conf import settings

dbHost = settings.DATABASES['default']['HOST']
dbUsername = settings.DATABASES['default']['USER']
dbPassword = settings.DATABASES['default']['PASSWORD']
dbName = settings.DATABASES['default']['NAME']

def connectDatabase():
    return pymysql.connect(host=dbHost,user=dbUsername,passwd=dbPassword,db=dbName)
    