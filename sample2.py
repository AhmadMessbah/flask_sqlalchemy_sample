from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(20))

    posts = relationship("Post", back_populates="users")


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String(100))

    users = relationship("User", back_populates="posts")


engine = create_engine("mysql+pymysql://root:root123@localhost:3306/mft")

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# user = User()
# user.name = "ahmad"
# session.add(user)

post = Post()
post.title = "SqlAlchemy"
session.add(post)

user = session.get(User,1)
# post = session.get(Post,1)

user.posts.append( post)

session.commit()

# user = session.query(User).get(user_id)
# post = session.query(Article).get(post_id)
#
# user.posts.remove(post)
# post.users.remove(user)
#
# session.commit()
