from django.db import models

# Create your models here.
class Comment:
    comment = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    show_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
