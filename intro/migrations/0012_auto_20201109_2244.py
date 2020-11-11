# Generated by Django 3.1 on 2020-11-09 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic=False
    dependencies = [
        ('intro', '0011_comment_discoverbook_rating_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendationList',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=200)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intro.book')),
            ],
        ),
        migrations.RemoveField(
            model_name='rating',
            name='discoverbook',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='DiscoverBook',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
