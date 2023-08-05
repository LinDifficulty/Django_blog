from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class BoardModel(models.Model):
    name = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'board'

    def __str__(self):
        return f"{self.name}-----{self.is_active}"


class PostModel(models.Model):
    title = models.CharField(max_length=15, null=False)
    content = models.TextField(null=False)
    create_time = models.DateTimeField(default=datetime.now)
    read_count = models.IntegerField(default=0)
    is_topping = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    board = models.ForeignKey(BoardModel, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        db_table = 'post'

    def __str__(self):
        return f"{self.title}-----{self.author.username}-----{self.is_active}"
