from model.entity.user import User
from model.repository.database_manager import DatabaseManager


class UserRepository(DatabaseManager):
    def find_by_username(self, username):
        self.make_engine()
        self.session.query(User).filter (User.name == username)