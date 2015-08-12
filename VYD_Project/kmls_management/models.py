from django.db import models

# Create your models here.
class Kml(models.Model):
    file = models.FileField(upload_to='./kmls_management/static')
    visibility = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.file.name.split("/")[2])

    def get_visivility(self):
        return self.visibility



