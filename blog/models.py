"""The models set the foundation of data that can then
be viewed and edited by admin and users. Below are the
models for blog posts and user comments allowing for
CRUD functionality. These models are called on in the view"""

from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0, "Draft"),
    (1, "Published")
)


class Post(models.Model):
    """Post model sets the attributes to be included in each
    post and their limitations like title length. Cascade
    is used to ensure asscociated data with a post is also
    deleted when deleted"""

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
