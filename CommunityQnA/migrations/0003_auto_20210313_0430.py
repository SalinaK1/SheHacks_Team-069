# Generated by Django 3.1.7 on 2021-03-13 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CommunityQnA', '0002_auto_20210313_0354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qna',
            name='id',
        ),
        migrations.AlterField(
            model_name='qna',
            name='question_no',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]