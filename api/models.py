from django.db import models

# Create your models here.
class Version(models.Model):
    version = models.CharField(max_length=25)
    build_to = models.IntegerField(max_length=14)
    build_from = models.IntegerField(max_length=14)
    pub_date = models.DateField(auto_now=True)
    version_to = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    git_hash = models.CharField(max_length=255)

    # def __unicode__(self):
    #     return self.md5hash