from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Editorial(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

