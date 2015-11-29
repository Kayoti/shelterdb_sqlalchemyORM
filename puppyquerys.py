from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from puppies import Base, Shelter, Puppy
#from flask.ext.sqlalchemy import SQLAlchemy
from random import randint
import datetime
import random

engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


#Add Shelters
query_obj1=session.query(Puppy).all()

for item in query_obj1:
	print item.name
print '\n\n\n'
today = datetime.date.today()
days_old = 180
birthday = today - datetime.timedelta(days = days_old)
query_obj1=session.query(Puppy).order_by(Puppy.dateOfBirth).filter(and_(Puppy.dateOfBirth > birthday , Puppy.dateOfBirth < today))
for item in query_obj1:
	print item.name
	print '---'
	print item.dateOfBirth
