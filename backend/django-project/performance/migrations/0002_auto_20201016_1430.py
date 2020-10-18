# Generated by Django 3.1.2 on 2020-10-16 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('comment', models.TextField(default=None, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('competences', models.IntegerField(default=None)),
                ('justice', models.TextField(default=None, max_length=255)),
                ('grade', models.TextField(default=None, max_length=255)),
                ('court', models.TextField(default=None, max_length=255)),
                ('court_class', models.TextField(default=None, max_length=255)),
                ('subject', models.TextField(default=None, max_length=255)),
                ('judging_body', models.TextField(default=None, max_length=255)),
                ('amount_of_varas', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='StepConfiguration',
            fields=[
                ('step_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('origin', models.TextField(default=None, max_length=255)),
                ('destination', models.TextField(default=None, max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='vara',
            name='id',
        ),
        migrations.AddField(
            model_name='vara',
            name='days_finish_process',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='vara',
            name='finished_processes',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='vara',
            name='movements',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='vara',
            name='ranking',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='vara',
            name='time_macrostep_1',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='vara',
            name='time_macrostep_2',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='vara',
            name='time_macrostep_3',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='vara',
            name='time_macrostep_4',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='vara',
            name='vara_id',
            field=models.BigIntegerField(default=-1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vara',
            name='latitude',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='vara',
            name='longitude',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='vara',
            name='name',
            field=models.TextField(default=None, max_length=255),
        ),
        migrations.CreateModel(
            name='VaraList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default=None, max_length=255)),
                ('vara_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performance.vara')),
            ],
        ),
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_time', models.IntegerField(default=None)),
                ('med_time', models.IntegerField(default=None)),
                ('max_time', models.IntegerField(default=None)),
                ('frequency', models.IntegerField(default=None)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performance.comments')),
                ('step_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performance.stepconfiguration')),
                ('vara_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performance.vara')),
            ],
        ),
        migrations.AddField(
            model_name='vara',
            name='group_id',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='performance.group'),
            preserve_default=False,
        ),
    ]
