from django.contrib import admin
from . import models
# Register your models here.

class PodopiecznyMemberInLine(admin.TabularInline):
    model = models.PodopiecznyMember

admin.site.register(models.Podopieczny)
