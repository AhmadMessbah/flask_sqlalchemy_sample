from model.entity.user import User
from model.service.user_service import UserService


class UserController:
    @classmethod
    def save(cls, name, family, username, password):
        user = User(name, family, username, password)
        UserService.save(user)
        return user
