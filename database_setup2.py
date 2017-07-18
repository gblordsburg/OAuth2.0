import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    email = Column(String(250))
    picture = Column(String(250))

    @property
    def serialize(self):
        #Returns object data in easily serializable format
        return {
        'name' : self.name,
        'email' : self.email,
        'picture' : self.picture,
        'id' : self.id
        }


class Restaurant(Base):
    __tablename__ = 'restaurant'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
        'name' : self.name,
        'id' : self.id,
        }


class MenuItem(Base):
    __tablename__ = 'menu_item'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    #Looks in restaurant table and retrieves the id number#
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    #variable restaurant is the relationship between the class Relationship#
    restaurant = relationship(Restaurant)
    user = relationship(User)

    @property
    def serialize(self):
        #Returns object data in easily serializable format
        return {
        'name' : self.name,
        'description' : self.description,
        'id' : self.id,
        'price' :self.price,
        'course' :self.course,
        }


engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)
