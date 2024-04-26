from django.db import models

class UserModel(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.username
    class Meta:
        db_table = 'ezy_users'