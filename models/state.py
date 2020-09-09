#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv('HBTN_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City', cascade='all, delete-orphan', backref='state')

    else:
        @property
        def cities(self):
            '''Returns list of cities where dstate_id is equal to State.id'''
            all_cities = models.storage.all(City)
            instance_list = []
            for key, val in all_cities.items():
                if self.id == val.state_id:
                    instance_list.append(val)
            return instance_list
