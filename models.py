from django.db import models

class Language(models.Model):
    '''A model for storing a language'''
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __unicode__(self):
        return '%s: %s' % (self.code, self.name)

class TextItemName(models.Model):
    '''A model for storing the name of a piece of text, used to select one
    piece of text but in multiple languages.'''
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    def get_depth(self, divider='_'):
        return len(self.name.split(divider))

class TextItem(models.Model):
    '''The individual text item, belongs to a name and has a language.
    '''
    name = models.ForeignKey(TextItemName)
    language = models.ForeignKey(Language)
    content = models.TextField()
    is_markdown = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s (%s)' % (self.name.name, self.language.code)


####################################################
############### Common model lookups ###############
####################################################

def textspace(namespace, language, depth=None):
    '''Uses the beginning of name strings and a language to retrieve all the
    text items that share the same root in their name. Returns a dictionary
    with the form:
        {
        'text_item_name':'text_item_content',
        }
    Can be used to quickly add text items to a context and then use them
    directly in templates.
    '''
    objs = TextItem.objects.filter(name__name__startswith=namespace, language__code=language)
    d = {}
    for t in objs:
        if depth:
            if not t.name.get_depth() > depth:
                d[t.name.name] = t.content
        else:
            d[t.name.name] = t.content
    return d

def text_item(name, language):
    '''Returns the content of a single text item, using the name and
    language.'''
    objs = TextItem.objects.filter(name__name=name, language__code=language)
    if objs:
        return objs[0].content
    else:
        return 'Missing Translation'

def text_by_lang(name):
    '''Returns a list of tuples based on a text item name, each tuple has the
    form:
        (language_code, content)
    '''
    objs = TextItem.objects.filter(name__name=name)
    d = []
    for t in objs:
        d.append((t.language.code, t.content))
    return {name:d}




