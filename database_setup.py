import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class User(Base) :
	__tablename__ = 'user'
	name = Column(String(80), nullable = False)
	email = Column(String(80), nullable = False)
	picture = Column(String(250), nullable = False)
	id = Column(Integer, primary_key = True)

	@property
	def serialize(self):
	    return {
	    	'name' : self.name,
	    	'email' : self.email,
	    	'picture' : self.picture,
	    	'id' : self.id,
	    }
	
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

	@property
	def serialize(self):
		#returns object data in easily serializable format
		return {
			'name' : self.name,
			'link' : self.link,
			'neighborhood' : self.neighborhood,
			'street' : self.street,
			'city' : self.city,
			'state' : self.state,
			'zipcode' : self.zipcode,
			'foodtype' : self.foodtype,
			'id' : self.id,
		}
	
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
			'course' : self.course,
			'description' : self.description,
			'price' : self.price,
			'id' : self.id,
		}

engine = create_engine('sqlite:///phillyrestaurants.db')

Base.metadata.create_all(engine)