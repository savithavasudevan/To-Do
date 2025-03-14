# Generated by Django 5.1.4 on 2025-03-11 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_taskmodel_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='due_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='priority_level',
            field=models.CharField(choices=[('high', 'high'), ('medium', 'medium'), ('low', 'low')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='is_completed',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='task_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
