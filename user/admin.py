from django.contrib import admin
from user.models import User, MasterProfile, MasterService
# Register your models here.
admin.site.register(User)
admin.site.register(MasterProfile)
admin.site.register(MasterService)