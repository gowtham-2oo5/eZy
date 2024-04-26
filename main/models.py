from django.db import models

class UserModel(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.username
    class Meta:
        db_table = 'ezy_users'
        
class EzySurveys(models.Model):
    surveyID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    createdBy = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    class Meta:
        db_table = 'ezy_surveys'

class EzySurveyQuestions(models.Model):
    questionID = models.AutoField(primary_key=True)
    surveyID = models.ForeignKey(EzySurveys, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    q_type = models.CharField(max_length=20)
    # q_options = models.JSONField(default=list)  # For PostgreSQL, equivalent to VARCHAR(20)[]
    class Meta:
        db_table = 'ezy_survey_questions'

class EzyResponses(models.Model):
    responseID = models.AutoField(primary_key=True)
    questionID = models.ForeignKey(EzySurveyQuestions, on_delete=models.CASCADE)
    response_text = models.CharField(max_length=255)
    response_option = models.CharField(max_length=255)
    class Meta:
        db_table = 'ezy_responses'