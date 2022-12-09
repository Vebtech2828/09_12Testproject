from django.contrib import admin
from test1.models import db123


class db123Admin(admin.ModelAdmin):
    list_display = ['eid', 'ename', 'esal', 'eaddr']

admin.site.register(db123,db123Admin)
