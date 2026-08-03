from django.db import models

class Notification(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    time=models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title
