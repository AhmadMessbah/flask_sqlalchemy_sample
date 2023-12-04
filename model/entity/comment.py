from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from model.entity import *


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id"))
    text = Column(String(100))

    post = relationship("Post", back_populates="comments")
