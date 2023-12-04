from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates

from model.entity import *


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    family = Column(String(30))
    username = Column(String(20))
    password = Column(String(20))

    posts = relationship("Post", back_populates="user")
    comments = relationship("Comment", back_populates="user")
    likes = relationship("Like", back_populates="user")

    def __init__(self,name,family,username,password):
        self.name = name
        self.family = family
        self.username = username
        self.password = password

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name