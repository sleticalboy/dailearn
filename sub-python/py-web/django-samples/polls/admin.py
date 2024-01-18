from django.contrib import admin

from . import models

# Register your models here.
# 在管理端可以看到并管理这些数据
admin.site.register([models.Question, models.Choice])
