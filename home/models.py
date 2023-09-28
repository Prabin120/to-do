from django.db import models

# Create your models here.
class Todo(models.Model):

    STATUS = (
        ('nd','Not Done'),
        ("d",'Done')
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=2, choices=STATUS,default='nd')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title