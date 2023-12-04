from model.entity.post import Post
from model.repository.post_repository import PostRepository


class PostService:
    @classmethod
    def save(cls, post):
        repository = PostRepository()
        repository.save(post)

    @classmethod
    def edit(cls, post):
        repository = PostRepository()
        return repository.edit(post)

    @classmethod
    def remove(cls, post_id):
        repository = PostRepository()
        post = repository.remove(post_id)
        return post

    @classmethod
    def find_all(cls):
        repository = PostRepository()
        return repository.find_all(Post)

    @classmethod
    def find_by_id(cls, post_id):
        repository = PostRepository()
        return repository.find_by_id(post_id)
