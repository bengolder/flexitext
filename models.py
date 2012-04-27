from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __unicode__(self):
        return '%s: %s' % (self.code, self.name)

class TextItemName(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    def get_depth(self, divider='_'):
        return len(self.name.split(divider))

class TextItem(models.Model):
    name = models.ForeignKey(TextItemName)
    language = models.ForeignKey(Language)
    content = models.TextField()
    is_markdown = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s (%s)' % (self.name.name, self.language.code)


