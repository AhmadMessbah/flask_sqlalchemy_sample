from model.entity.post import Post
from model.repository.database_manager import DatabaseManager


class PostRepository(DatabaseManager):
    def find_by_text(self, text):
        self.make_engine()
        return self.session.query(Post).filter(Post.text.like(f"%{text}%")).all()
