from django.db import models

# Create your models here.
class Kml(models.Model):
    name = models.CharField(max_length=50)

    visibility = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.name)

    def get_visivility(self):
        return self.visibility

    def get_name(self):
        return self.name


