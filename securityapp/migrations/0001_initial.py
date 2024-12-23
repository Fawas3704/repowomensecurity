# Generated by Django 5.1.3 on 2024-11-18 06:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=30, null=True)),
                ('Password', models.CharField(blank=True, max_length=30, null=True)),
                ('TYPE', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(blank=True, max_length=30, null=True)),
                ('Lastname', models.CharField(blank=True, max_length=30, null=True)),
                ('Age', models.IntegerField(blank=True, null=True)),
                ('place', models.CharField(blank=True, max_length=30, null=True)),
                ('Post', models.CharField(blank=True, max_length=30, null=True)),
                ('Pin', models.IntegerField(blank=True, null=True)),
                ('Number', models.BigIntegerField(blank=True, null=True)),
                ('Email', models.CharField(blank=True, max_length=30, null=True)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='securityapp.logintable')),
            ],
        ),
        migrations.CreateModel(
            name='FriendTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FriendName', models.CharField(blank=True, max_length=30, null=True)),
                ('Number', models.BigIntegerField(blank=True, null=True)),
                ('EmergencyNumber', models.BigIntegerField(blank=True, null=True)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='securityapp.usertable')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rating', models.CharField(blank=True, max_length=30, null=True)),
                ('Feedback', models.CharField(blank=True, max_length=100, null=True)),
                ('Date', models.DateTimeField(blank=True, null=True)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='securityapp.usertable')),
            ],
        ),
        migrations.CreateModel(
            name='ComplaintTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Complaint', models.CharField(blank=True, max_length=100, null=True)),
                ('Reply', models.CharField(blank=True, max_length=100, null=True)),
                ('Date', models.DateTimeField(blank=True, null=True)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='securityapp.usertable')),
            ],
        ),
    ]
