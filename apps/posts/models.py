from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.user', related_name='posts', on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=50)
    question = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}: {self.question}'
    
    class Meta:
        ordering = ['pub_date']