# Generated by Django 5.0.2 on 2024-04-26 12:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EzySurveyQuestions',
            fields=[
                ('questionID', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=100)),
                ('q_type', models.CharField(max_length=20)),
                ('q_options', models.JSONField(default=list)),
            ],
            options={
                'db_table': 'ezy_survey_questions',
            },
        ),
        migrations.CreateModel(
            name='EzyResponses',
            fields=[
                ('responseID', models.AutoField(primary_key=True, serialize=False)),
                ('response_text', models.CharField(max_length=255)),
                ('response_option', models.CharField(max_length=255)),
                ('questionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ezysurveyquestions')),
            ],
            options={
                'db_table': 'ezy_responses',
            },
        ),
        migrations.CreateModel(
            name='EzySurveys',
            fields=[
                ('surveyID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.usermodel')),
            ],
            options={
                'db_table': 'ezy_surveys',
            },
        ),
        migrations.AddField(
            model_name='ezysurveyquestions',
            name='surveyID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ezysurveys'),
        ),
    ]
