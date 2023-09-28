from django.db import models

# Create your models here.

class Page (models.Model):
    title = models.CharField(verbose_name= "Titulo", max_length=200)
    content = models.TextField(verbose_name = "Contenido")
    created = models.DateTimeField (auto_now_add=True, verbose_name= "Fecha de creacion") 
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")


    class meta:
        verbose_name = "pagina"
        verbose_name_plural = "paginas"
        ordening = ['title']  

        def __str__(self):
            return self.title
