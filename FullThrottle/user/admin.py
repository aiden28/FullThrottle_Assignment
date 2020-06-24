from django.contrib import admin

from .models import Activity,Member

# Register your models here.
admin.site.register(Member)
admin.site.register(Activity)
