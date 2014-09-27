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


class GcsVersion(models.Model):
    version_build = models.CharField(max_length=25)
    version_target = models.CharField(max_length=255)
    build_from = models.IntegerField(max_length=14)
    build_target = models.IntegerField(max_length=14)
    statue = models.IntegerField(max_length=6)
    submit_date = models.DateField(auto_now=True)
    file_server = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    md5_hash = models.CharField(max_length=255)
    git_hash = models.CharField(max_length=255)
    describe = models.CharField(max_length=255)
    more_url = models.CharField(max_length=255)
