from django.db import models



# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title
    
    objects = models.Manager()
    #오 이거 넣으니까 해결 됐네

    def summary(self):
        return self.body[:100] #pylint: disable=E1136
    