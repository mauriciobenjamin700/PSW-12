from django.contrib import admin


from apps.shortener.models import *


admin.site.register(Links)
admin.site.register(Clicks)