# Generated by Django 4.1.7 on 2024-01-03 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0010_alter_wordscore_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordSoundMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=1000)),
                ('region', models.CharField(max_length=100, null=True)),
                ('soundmark', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RemoveIndex(
            model_name='wordpronounce',
            name='WordPronounce_word_idx',
        ),
        migrations.RemoveField(
            model_name='wordpronounce',
            name='soundmark',
        ),
        migrations.RemoveField(
            model_name='wordpronounce',
            name='source',
        ),
        migrations.AddField(
            model_name='wordpronounce',
            name='pronounceBase64',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='wordpronounce',
            name='region',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddIndex(
            model_name='wordpronounce',
            index=models.Index(fields=['word', 'region'], name='WordPronounce_word_region'),
        ),
        migrations.AddConstraint(
            model_name='wordpronounce',
            constraint=models.UniqueConstraint(fields=('word', 'region'), name='WordPronounce_unique'),
        ),
        migrations.AddIndex(
            model_name='wordsoundmark',
            index=models.Index(fields=['word', 'region'], name='WordSoundMark_word_region'),
        ),
        migrations.AddConstraint(
            model_name='wordsoundmark',
            constraint=models.UniqueConstraint(fields=('word', 'region'), name='WordSoundMark_unique'),
        ),
    ]
