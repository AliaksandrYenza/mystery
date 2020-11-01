from django.db import models

# Create your models here.


class Artiles(models.Model):
    title = models.CharField('name', max_length=50, default= 'N/A Note')
    intro = models.CharField('intro', max_length= 250)
    description = models.TextField('full')
    date = models.DateTimeField('date')

    def __str__(self):
        return f'Note: {self.title}\n'

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'