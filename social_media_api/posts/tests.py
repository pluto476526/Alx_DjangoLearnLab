from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post, Comment

class PostCommentTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='user001', password='12341234')
        self.post = Post.objects.create(author=self.user, title='post 2', content='some blog content')

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'post 2')

    def test_comment_creation(self):
        comment = Comment.objects.create(post=self.post, author=self.user, content='nice stuff')
        self.assertEqual(comment.content, 'nice stuff')

