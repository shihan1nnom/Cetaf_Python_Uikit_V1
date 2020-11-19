from django.db import models

# Create your models here.


class Sede(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Ambiente(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Activo(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    num_serie = models.CharField(max_length=50)
    fecha_compra = models.DateField()
    cobertura_seguro = models.CharField(max_length=200)
    valor_compra = models.IntegerField(default=0)
    garantia = models.CharField(max_length=200)
    fecha_puesto_servicio = models.DateField()
    descripcion = models.TextField()
    vida_util = models.CharField(max_length=200)
    valor_residual = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre


class Asignacion(models.Model):
    nombre_activo = models.ForeignKey(Activo, on_delete=models.CASCADE)
    persona_responsable = models.CharField(max_length=50)
    sede_asignada = models.ForeignKey(Sede, on_delete=models.CASCADE)
    ambiente_asignado = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return self.persona_responsable
