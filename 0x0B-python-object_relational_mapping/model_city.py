#!/usr/bin/python3
"""
Module contains the class city
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base


class City(Base):
    """
    class city that contains the cities
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
