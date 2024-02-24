from django.db import models
import random
import string

class MiniURL(models.Model):
    urlLongue = models.URLField(verbose_name="URL à réduire", unique=True)
    code = models.CharField(max_length=6, unique=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date d'enregistrement")
    pseudo = models.CharField(max_length=255, blank=True, null=True)
    nb_acces = models.IntegerField(default=0, verbose_name="Nombre d'accès l'url")

    def __str__(self):
        return "[{0}] {1}".format(self.code, self.urlLongue)
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.generer(6)

        super(MiniURL, self).save(*args, **kwargs)

    def generer(nb_caracteres):
        caracteres = string.ascii_letters + string.digits
        aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]

        return ''.join(aleatoire)

    class Meta:
        verbose_name = "Mini URL"
        verbose_name_plural = "Minis URL"