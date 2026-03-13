from django.db import models

class Books(models.Model):
    name_book = models.CharField(max_length=50, verbose_name='укажите название книги')
    description = models.TextField(verbose_name='укажите описание книги')
    image = models.ImageField(upload_to='books/', verbose_name='загрузите обложку')

    CATEGORY_BOOK = (
        ('фантастика', 'фантастика'),
        ('хоррор', 'хоррор'),
        ('исторические', 'исторические')
    )

    category_book = models.CharField(max_length=100, choices=CATEGORY_BOOK, 
                                     verbose_name='выберите категорию')
    
    url_audio_book = models.URLField(verbose_name='укажите ссылку на аудиокнигу')

    #Логика для просмотров
    views = models.PositiveIntegerField(default=0, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_book

    class Meta:
        verbose_name = 'книгу'
        verbose_name_plural = 'книги'