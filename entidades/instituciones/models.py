from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=150, primary_key=True)
    s = models.CharField(max_length=160)

    def save(self, *args, **kwargs):
        self.s = slugify(self.nombre)
        super(Institucion, self).save(*args, **kwargs)

class Programa(models.Model):
    nombre = models.CharField(max_length=150)
    institucion = models.ForeignKey(Institucion, related_name="get_programas", on_delete=models.PROTECT)

class Inscrito(models.Model):
    nombre = models.CharField(max_length=150)
    institucion = models.ForeignKey(Institucion, related_name="get_inscritos", on_delete=models.PROTECT)
    programas = models.ManyToManyField(Programa)

    

