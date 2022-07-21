import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User (Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(220), nullable=False)
    password = Column(String(10), nullable=False)
    vehicles= relationship("Vehicles")


class Vehicles (Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey("user.id"))
    user= relationship("User", back_populates="children")
    cars = relationship("Car", back_populates="parent")
    motorcicles = relationship("Motorcicle")

class Car(Base):
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True)
    color = Column(String(220), nullable=False)
    vehicles_id = Column(Integer, ForeignKey("vehicles.id"))
    vehicles = relationship("Vehicles")

class Motorcicle(Base):
    __tablename__ = 'motorcicle'
    id = Column(Integer, primary_key=True)
    color = Column(String(220), nullable=False)
    year = Column(String(220), nullable=False)
    vehicles_id = Column(Integer, ForeignKey("vehicles.id"))
    vehicles = relationship("Vehicles")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')