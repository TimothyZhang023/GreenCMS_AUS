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
    #build is number 20140928
    #version like string v2.5.11.01
    build = models.IntegerField(max_length=14)
    version = models.CharField(max_length=100)

    version_from = models.CharField(max_length=100)
    version_target = models.CharField(max_length=100)

    build_from = models.IntegerField(max_length=14)
    build_target = models.IntegerField(max_length=14)

    # 1 for ok , 0 for need approval ,2 for phase ,3 for reject ,4 for unload , 5 for delete
    statue = models.IntegerField(max_length=6)

    #grenerated by db
    submit_date = models.DateField(auto_now=True)

    #grenerated by conf
    file_server = models.CharField(max_length=255)

    #grenerated by info
    file_name = models.CharField(max_length=255)

    #grenerated auto
    md5_hash = models.CharField(max_length=255)

    #to gen github links
    git_hash = models.CharField(max_length=255)

    #description for upgrade
    description = models.CharField(max_length=255)

    #extra url
    more_url = models.CharField(max_length=255)


class GcsTheme(models.Model):
    #build is number 20140928
    #version like string v2.5.11.01
    theme_name = models.CharField(max_length=255)
    build = models.IntegerField(max_length=14)
    version = models.CharField(max_length=100)

    # author
    author = models.CharField(max_length=255)

    #grenerated auto
    md5_hash = models.CharField(max_length=255)

    #grenerated by db
    submit_date = models.DateField(auto_now=True)

    # 1 for ok , 0 for need approval ,2 for phase ,3 for reject ,4 for unload , 5 for delete
    statue = models.IntegerField(max_length=6)

    #grenerated by conf
    file_server = models.CharField(max_length=255)

    #grenerated by info
    file_name = models.CharField(max_length=255)

    #description for theme
    description = models.CharField(max_length=255)

    #extra url
    more_url = models.CharField(max_length=255)

class GcsPlugin(models.Model):
    #build is number 20140928
    #version like string v2.5.11.01
    plugin_name = models.CharField(max_length=255)
    build = models.IntegerField(max_length=14)
    version = models.CharField(max_length=100)

    # author
    author = models.CharField(max_length=255)

    #grenerated auto
    md5_hash = models.CharField(max_length=255)

    #grenerated by db
    submit_date = models.DateField(auto_now=True)

    # 1 for ok , 0 for need approval ,2 for phase ,3 for reject ,4 for unload , 5 for delete
    statue = models.IntegerField(max_length=6)

    #grenerated by conf
    file_server = models.CharField(max_length=255)

    #grenerated by info
    file_name = models.CharField(max_length=255)

    #description for plugin
    description = models.CharField(max_length=255)

    #extra url
    more_url = models.CharField(max_length=255)
