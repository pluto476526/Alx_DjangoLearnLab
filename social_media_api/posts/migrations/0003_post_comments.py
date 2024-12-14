# Generated by Django 5.1.4 on 2024-12-14 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_uploaded_at_comment_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='comments', to='posts.comment'),
        ),
    ]
