from django.db import models


class Pracownicy(models.Model):
	imie = models.CharField(max_length=20)
	nazwisko = models.CharField(max_length=30)
	stanowisko = models.CharField(max_length=20)
	etat = models.SmallIntegerField(default=0)

	def zapisz(self):
		self.save()

# Create your models here.
