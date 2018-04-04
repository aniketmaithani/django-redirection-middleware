from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import Redirection


@admin.register(Redirection)
class RedirectionAdmin(VersionAdmin):
    pass
