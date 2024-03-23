from django.db import models
from authApp.models import eZy_users

class user_forms(models.Model):
    form_id = models.AutoField(primary_key=True)
    form_name = models.CharField(max_length=100)
    form_desc = models.CharField(max_length=1000)
    form_created = models.DateTimeField('date created')
    form_updated = models.DateTimeField('date updated')
    form_status = models.BooleanField(default=True)
    form_owner = models.CharField(max_length=100)
    class Meta:
        db_table = 'user_forms'
class form_questions(models.Model):
    form_id = models.ForeignKey(user_forms, on_delete=models.CASCADE)
    question_id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=1000)
    question_type = models.CharField(max_length=100)
    question_required = models.BooleanField(default=False)
    class Meta:
        db_table = 'form_questions'
        
class form_answers(models.Model):
    form_id = models.ForeignKey(user_forms, on_delete=models.CASCADE)
    question_id = models.ForeignKey(form_questions, on_delete=models.CASCADE)
    user_id = models.ForeignKey(eZy_users, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=1000)
    class Meta:
        db_table = 'form_answers'
        
class grievances(models.Model):
    grievance_id = models.AutoField(primary_key=True)
    grievance_user = models.CharField(max_length=100)
    grievance_issue = models.CharField(max_length=100)
    grievance_message = models.CharField(max_length=1000)
    class Meta:
        db_table = 'grievances'