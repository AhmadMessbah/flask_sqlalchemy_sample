from model.entity.user import User
from model.repository.user_repository import UserRepository


class UserService:
    @classmethod
    def save(cls, user):
        repository = UserRepository()
        repository.save(user)

    @classmethod
    def edit(cls, user):
        repository = UserRepository()
        return repository.edit(user)

    @classmethod
    def remove(cls, user_id):
        repository = UserRepository()
        user = repository.remove(user_id)
        return user

    @classmethod
    def find_all(cls):
        repository = UserRepository()
        return repository.find_all(User)

    @classmethod
    def find_by_id(cls, user_id):
        repository = UserRepository()
        return repository.find_by_id(User,user_id)
