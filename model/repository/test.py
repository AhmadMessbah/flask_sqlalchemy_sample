from controller.user_controller import UserController
from model.entity import Comment
from model.entity.like import Like
from model.entity.post import Post
from model.entity.user import User
from model.repository.database_manager import DatabaseManager
from model.repository.post_repository import PostRepository
from model.repository.user_repository import UserRepository
from model.service.post_service import PostService
from model.service.user_service import UserService

user = User("AA","BB","CC","DD")
user.name = "ahmad"

post = Post()
post.text = "post"

user.posts.append(post)

user1 = User("A","B","C","D")
user1.name = "fan"

comment1 = Comment()
comment1.text = "comment1"
comment1.user = user
post.comments.append(comment1)

comment2 = Comment()
comment2.text = "comment2"
comment2.user=user1
post.comments.append(comment2)

like1 = Like()
like1.post = post
like1.user = user1

like2 = Like()
like2.post = post
like2.user=user1

em = DatabaseManager()
em.make_engine()
em.session.add(user)
em.session.add(post)
em.session.add(comment1)
em.session.add(comment2)
em.session.add(like1)
em.session.add(like2)
em.session.commit()

for user in UserService.find_all():
    print(user.json())
    for post in user.posts:
        print(post.json())
        for comment in post.comments:
            print(comment.json())

        for like in post.likes:
            print(like.json())


# user = UserController.save("ahmad","messbah","ahmad","ahamd123")
# print(user.id)

# user = User()
# user.name = "new"
#
# UserService.save(user)
# print(user.id)
#
# post = Post()
# post.text = "Text new"
#
# PostService.save(post)
# print(post.id)

#
# repo = UserRepository()
# user = repo.find_by_id(User,1)
# repo.save(user)
#
# print(user)
# print(user.name)
#
# post = Post()
# post.text = "text"

# repo = PostRepository()
# repo.save(post)

# print(repo.find_all(Post))
# post = repo.find_by_text("x")
# print(post[0].text)

# em = DatabaseManager()
# em.save(user)
# print(user.id)

# post = Post()
# post.title = "SqlAlchemy2"
# em = DatabaseManager()
# em.make_engine()
# em.save(post)
# print(post.id)
#
# em = DatabaseManager()
# user = em.session.get(User,1)
# post = em.session.get(Post,1)
#
# user.posts.append(post)
#
# em.session.commit()

# user =  em.find_by_id(User,1)
# post =  em.find_by_id(Post,1)
#
# user.posts.append(post)
# em.session.commit()