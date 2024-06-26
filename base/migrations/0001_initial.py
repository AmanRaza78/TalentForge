# Generated by Django 4.2.11 on 2024-04-28 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('correct_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='correct_question', to='base.option')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('duration_minutes', models.IntegerField(default=30)),
                ('questions', models.ManyToManyField(to='base.question')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.skill')),
            ],
        ),
        migrations.CreateModel(
            name='TestAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.test')),
            ],
        ),
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.question')),
                ('selected_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.option')),
                ('test_attempt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.testattempt')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.skill'),
        ),
        migrations.AddField(
            model_name='option',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.question'),
        ),
    ]
