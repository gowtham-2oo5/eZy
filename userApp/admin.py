from django.contrib import admin
from .models import user_forms,form_questions,form_answers

admin.site.register(user_forms)
admin.site.register(form_questions)
admin.site.register(form_answers)