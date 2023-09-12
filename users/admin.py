from django.contrib import admin
from django.contrib.auth import get_user_model
from specialists.models import Specialist
from procedures.models import Procedure

# Register your models here.


# class AuthorAdmin(admin.ModelAdmin):
#     pass
admin.site.register(get_user_model())
admin.site.register(Specialist)
admin.site.register(Procedure)