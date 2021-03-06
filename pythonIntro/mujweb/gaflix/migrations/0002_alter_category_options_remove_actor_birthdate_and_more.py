# Generated by Django 4.0.1 on 2022-02-24 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gaflix', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='actor',
            name='birthDate',
        ),
        migrations.RemoveField(
            model_name='director',
            name='birthDate',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='csfdRating',
        ),
        migrations.AddField(
            model_name='actor',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='director',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, to='gaflix.Actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='categories',
            field=models.ManyToManyField(blank=True, to='gaflix.Category'),
        ),
        migrations.AddField(
            model_name='movie',
            name='csfd_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gaflix.director'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='actor',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='director',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
