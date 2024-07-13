from django.db import models

# Create your models here.

class History(models.Model):
    nome = models.CharField(max_length=20)
    history = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = 'Histories'