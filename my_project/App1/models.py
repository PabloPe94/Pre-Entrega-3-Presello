from django.db import models

# Create your models here.

class Interior(models.Model):

    

    nombre_cientifico = models.CharField(max_length = 100)
    nombre_comun = models.CharField(max_length = 100)
    tipo_de_luz = models.CharField(max_length = 15) #luz directa o indirecta
    riego_semanal = models.IntegerField() #cuantos riegos por semana
    foto = models.ImageField(upload_to="images/", default="images/default.jpg")

    def __str__(self):
        return f"Nombre Cientifico: {self.nombre_cientifico} Nombre Comun: {self.nombre_comun} Tipo de Luz: {self.tipo_de_luz} Riego Semanal: {self.riego_semanal}"

class Exterior(models.Model):

    nombre_cientifico = models.CharField(max_length = 100)
    nombre_comun = models.CharField(max_length = 100)
    tipo_de_clima = models.CharField(max_length = 30) #arido, tropical, templado, polar
    riego_semanal = models.IntegerField() #cuantos riegos por semana
    ciudados_especiales = models.CharField(max_length = 400)
    foto = models.ImageField(upload_to="images/", default="images/default.jpg")
    def __str__(self):
        return f"Nombre Cientifico: {self.nombre_cientifico} Nombre Comun: {self.nombre_comun}"
class Carnivora(models.Model):
    nombre_cientifico = models.CharField(max_length = 100)
    nombre_comun = models.CharField(max_length = 100)
    tipo_de_clima = models.CharField(max_length = 30) #arido, tropical, templado, polar
    riego_semanal = models.IntegerField() #cuantos riegos por semana
    ciudados_especiales = models.CharField(max_length = 400)
    alimentacion = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="images/", default="images/default.jpg")
    def __str__(self):
        return self.nombre_comun

class Usuario(models.Model):
    
    nombre = models.CharField(max_length=30)
    nombre_usuario = models.CharField(max_length=15)
    email = models.EmailField()




