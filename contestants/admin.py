from django.contrib import admin
from .models import ContestType, ContestantForm


# Register your models here.
admin.site.register(ContestType)
admin.site.register(ContestantForm)