# Generated by Django 2.2 on 2021-09-16 11:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
                ('liked', models.ManyToManyField(blank=True, related_name='liked', to='profiles.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralPost',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='posts.Post')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=360)),
                ('image', models.ImageField(blank=True, upload_to=posts.models.get_upload_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
            ],
            bases=('posts.post',),
        ),
        migrations.CreateModel(
            name='ProblemPost',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='posts.Post')),
                ('problem_reported', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.ProblemReported')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Report')),
            ],
            bases=('posts.post',),
        ),
    ]
