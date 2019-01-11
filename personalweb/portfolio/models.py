from django.db import models


# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        # public singular name
        verbose_name = 'Project'
        # public plural name
        verbose_name_plural = 'Projects'
        # ordering by created date inverted (-created) no inverted (created)
        ordering = ['-created']
