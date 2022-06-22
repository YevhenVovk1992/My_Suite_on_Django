from django.db import models

# Create your models here.
class Artiles(models.Model):
    title = models.CharField('Names', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('text')
    date = models.DateTimeField('Date')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'

class motors(models.Model):
    title = models.CharField('Brand', max_length=200)
    model = models.CharField('Model', max_length=250)
    photo = models.ImageField(upload_to='catalog/')
    content = models.TextField('About')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Motor'
        verbose_name_plural = 'Motors'
