from django.contrib import admin

# Register your models here.
from .models import FaceData, Presenty, Teacher,UserLog


admin.site.register(FaceData)
admin.site.register(UserLog)
admin.site.register(Teacher)
admin.site.register(Presenty)
