from django.db import models
from django.utils.text import slugify 

class Institucion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=160,default=None, blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.s = slugify(self.nombre, allow_unicode=True)
        super(Institucion, self).save(*args, **kwargs)

class Programa(models.Model):
    nombre = models.CharField(max_length=150)
    institucion = models.ForeignKey(Institucion, related_name="get_programas", on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

class Inscrito(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    institucion = models.ForeignKey(Institucion, related_name="get_inscritos", on_delete=models.PROTECT)
    programas = models.ManyToManyField(Programa)

    

