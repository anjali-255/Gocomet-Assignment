from django.db import models

class AllBlogs(models.Model):
    topic = models.CharField(max_length=500, null=True)
    title = models.CharField(max_length=500, null=True)
    date = models.CharField(max_length=500, null=True)
    details = models.CharField(max_length=500, null=True)
    author = models.CharField(max_length=120, null=True)

    def __str__(self):
        return self.title