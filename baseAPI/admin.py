from django.contrib import admin
from baseAPI.models import Snippet ,Emp
# Register your models here.

# admin.site.register(Snippet)

class SnippetTable(admin.ModelAdmin):
    list_display = ('created', 'title', 'code', 'linenos', 'language', 'style')
admin.site.register(Snippet,SnippetTable)


class EmpTable(admin.ModelAdmin):
    list_display = ('id','name','position','salary','start_date','office','extn')
admin.site.register(Emp,EmpTable)
