from django.contrib import admin

from . import models


# 在管理端可以看到并管理这些数据


# 不同的显示样式
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    # 几个选项
    extra = 3
    # 关联模型
    model = models.Choice
    pass


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('日期信息', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    # 显示那些列
    list_display = ['question_text', 'pub_date', 'was_recently']
    # 过滤器
    list_filter = ['pub_date']
    # 搜索字段
    search_fields = ['question_text']
    pass


# 在管理端注册并管理这些数据
admin.site.register(models.Question, QuestionAdmin)
