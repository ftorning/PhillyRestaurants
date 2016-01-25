#configuration code
#	generally shouldn't change from project to project
#at the beginning of the file
#	imports all modules needed
#	creates instance of declarative base
#at the end of the file
#	creates (or connects) the database and adds tables and columns

import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

#class code
#	representation of table as a python class
#	extends the Base class
#	nested inside will be table and mapper code
#table code
#	representation of our table inside the database
#	__tablename__ = 'some_table'
#mapper code
#	maps python objects to columns in our database
#	columnName = Column(attributes, ...)
#	examples:
#		String(250)
#		Integer
#		relationship(Class)
#		nullable = False
#		primary_key = True
#		ForeignKey('some_table.id')

class User(Base) :
	__tablename__ = 'user'
	name = Column(String(80), nullable = False)
	email = Column(String(80), nullable = False)
	picture = Column(String(250), nullable = False)
	id = Column(Integer, primary_key = True)

class Restaurant(Base) :
	__tablename__ = 'restaurant'
	name = Column(String(80), nullable = False)
	logo = Column(String(120), nullable = True)
	interior = Column(String(120), nullable = True)
	link = Column(String(120), nullable = True)
	neighborhood = Column(String(50), nullable = False)
	street = Column(String(120), nullable = False)
	city = Column(String(50), nullable = False)
	state = Column(String(50), nullable = False)
	zipcode = Column(String(50), nullable = False)
	foodtype = Column(String(120), nullable = False)
	id = Column(Integer, primary_key = True)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)
	MenuItems = relationship("MenuItem", cascade="all,delete")
	
class MenuItem(Base) :
	__tablename__ = 'menu_item'
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	course = Column(String(50))
	description = Column(String(500))
	price = Column(String(50))
	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
	restaurant = relationship(Restaurant)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
		#returns object data in easily serializable format
		return {
			'name' : self.name,
			'description' : self.description,
			'id' : self.id,
			'price' : self.price,
		}

engine = create_engine('sqlite:///phillyrestaurants.db')

Base.metadata.create_all(engine)