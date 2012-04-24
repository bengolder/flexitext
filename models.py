from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __unicode__(self):
        return '%s: %s' % (self.code, self.name)

class TextItem(models.model):
    name = models.CharField(max_length=200)
    language = models.ForeignKey(Language)
    content = models.TextField()
    is_markdown = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.language.code)


