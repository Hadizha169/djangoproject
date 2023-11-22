from django.db import models

class RunString(models.Model):
    title = models.CharField(max_length=100, verbose_name='Enter your title')
    description = models.TextField(verbose_name='Enter your description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бегущую строку'
        verbose_name_plural = 'Бегущие строки'


class GamePostModel(models.Model):
    GENRE = (
        ('Simulator', 'Simulator'),
        ('Quest', 'Quest')
    )
    title = models.CharField(max_length=100, verbose_name="Enter your game name")
    description = models.TextField()
    image = models.ImageField(upload_to='games/')
    cost = models.PositiveIntegerField()
    genre = models.CharField(max_length=100, choices=GENRE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Afisha(models.Model):
    title_game = models.CharField(max_length=100, null=True)
    time_title = models.TimeField()
    hall = models.CharField(max_length=10)

    def __str__(self):
        return self.title_game

class Slider(models.Model):
    photo = models.URLField()

    def __str__(self):
        return self.photo
