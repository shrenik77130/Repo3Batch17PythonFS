from django.contrib import admin
from .models import QuestionType,QuestionBank, ExamType, ExamMaster, ExamLog

# Register your models here.
admin.site.register(QuestionType)
admin.site.register(QuestionBank)
admin.site.register(ExamType)
admin.site.register(ExamMaster)
admin.site.register(ExamLog)
