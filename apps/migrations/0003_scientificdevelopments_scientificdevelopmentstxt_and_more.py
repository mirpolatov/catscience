# Generated by Django 4.2.8 on 2023-12-05 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_rename_maintxt_announcementdocuments_documents_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScientificDevelopments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ScientificDevelopmentsTxt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt', models.TextField()),
                ('developments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='developments_txt', to='apps.scientificdevelopments')),
            ],
        ),
        migrations.CreateModel(
            name='ScientificDevelopmentsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('developments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='developments_image', to='apps.scientificdevelopments')),
            ],
        ),
    ]
