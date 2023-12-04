from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from model.entity import *


class Like(Base):
    __tablename__ = "likes"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id"))

    post = relationship("Post", back_populates="likes")
