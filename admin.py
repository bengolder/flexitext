from flexitext.models import Language, TextItem, TextItemName
from django.contrib import admin

class TextItemInline(admin.StackedInline):
    model = TextItem

class TextItemNameAdmin(admin.ModelAdmin):
    inlines = [TextItemInline]

admin.site.register(Language)
admin.site.register(TextItemName, TextItemNameAdmin)
