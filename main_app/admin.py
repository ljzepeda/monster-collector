from django.contrib import admin
# import your models here
from .models import Monster, Battle, Type

# Register your models here.
admin.site.register(Monster)
admin.site.register(Battle)
admin.site.register(Type)