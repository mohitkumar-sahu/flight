from django.contrib import admin
from users.models import UserDetails,Status

# Register your models here.
admin.site.register(UserDetails)
admin.site.register(Status)