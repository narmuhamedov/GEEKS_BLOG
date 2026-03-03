from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Product(models.Model):
    title = models.CharField(max_length=100, default='ноутбук ACER')
    description = models.TextField(default='игровой ноутбук.......')
    photo = models.ImageField(upload_to='laptop', null=True)

    tags = models.ManyToManyField(Tag, null=True)

    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.title}: {', '.join(i.name for i in self.tags.all())}'

    # def __str__(self):
    #     return self.title.


class SerialNumber(models.Model):
    serial_number = models.OneToOneField(Product, on_delete=models.CASCADE)
    number  = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.serial_number} - {self.number}'
    


class ReviewProduct(models.Model):
    choice_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField(default='прикольный ноутбук')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice_product}-{self.comment}'
    
