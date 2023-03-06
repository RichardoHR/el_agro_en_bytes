from peewee import *
from decouple import config
import datetime


db = MySQLDatabase(
    'elagroenbytes_1',
    user = 'root',
    password = config('DBPASSWORD'),
    port= 3306,
    host = 'localhost'
)

class User(Model):
    username = TextField(unique = True, null = False)
    password = TextField(null = False)
    name = TextField()
    lastname = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        db_table = 'users'


db.create_tables([User])


#class Service(Model):
#    service_name = TextField(null = False)
#    created_by = TextField(null= False)
#    created_at = DateTimeField(default = datetime.datetime.now)

#    class Meta:
#        database = db
#        dn_table = 'services'


#db.create_tables([Service])


#class service_by_user(Model):
#    description = TextField(null=False)
#    service_id = foreign_key

    
    