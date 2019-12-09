from django.contrib import admin
from .models import Commission, ArchivedCommission
# Register your models here.

admin.site.register(Commission)
admin.site.register(ArchivedCommission)
