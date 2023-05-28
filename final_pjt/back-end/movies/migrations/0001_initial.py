# Generated by Django 3.2.18 on 2023-05-23 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActorList',
            fields=[
                ('actor', models.IntegerField(primary_key=True, serialize=False)),
                ('actor_id', models.IntegerField()),
                ('actor_name', models.CharField(max_length=1000)),
                ('actor_popularity', models.DecimalField(decimal_places=4, default=0, max_digits=1000000)),
                ('actor_revenue', models.DecimalField(decimal_places=4, default=0, max_digits=1000000)),
            ],
        ),
        migrations.CreateModel(
            name='AllMovie',
            fields=[
                ('adult', models.BooleanField()),
                ('backdrop_path', models.URLField(null=True)),
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('original_language', models.CharField(max_length=10)),
                ('overview', models.TextField()),
                ('popularity', models.DecimalField(decimal_places=4, max_digits=100000)),
                ('poster_path', models.URLField()),
                ('release_date', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('vote_average', models.DecimalField(decimal_places=3, max_digits=10)),
                ('vote_count', models.IntegerField(default=0)),
                ('eng_title', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='MovieDetail',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('budget', models.BigIntegerField(null=True)),
                ('revenue', models.BigIntegerField(null=True)),
                ('tagline', models.TextField(null=True)),
                ('adult', models.BooleanField(null=True)),
                ('backdrop_path', models.URLField(null=True)),
                ('homepage', models.URLField(null=True)),
                ('original_title', models.CharField(max_length=20, null=True)),
                ('overview', models.TextField(null=True)),
                ('popularity', models.DecimalField(decimal_places=3, default=0, max_digits=100000)),
                ('poster_path', models.URLField(null=True)),
                ('release_date', models.DateField(null=True)),
                ('runtime', models.IntegerField(null=True)),
                ('vote_average', models.DecimalField(decimal_places=3, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='TodayMovie',
            fields=[
                ('adult', models.BooleanField()),
                ('backdrop_path', models.URLField(null=True)),
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('original_language', models.CharField(max_length=10)),
                ('overview', models.TextField()),
                ('popularity', models.DecimalField(decimal_places=4, max_digits=100000)),
                ('poster_path', models.URLField()),
                ('release_date', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('vote_average', models.DecimalField(decimal_places=3, max_digits=10)),
                ('vote_count', models.IntegerField(default=0)),
                ('eng_title', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TodayMovieCreated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('today', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TodayRelatedVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.URLField(null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.todaymovie')),
            ],
        ),
        migrations.CreateModel(
            name='TodayGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_ids', models.CharField(max_length=50)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.todaymovie')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('star_score', models.FloatField()),
                ('user_profile_img', models.ImageField(null=True, upload_to='comment_profile_images/')),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.allmovie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AllRelatedVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.URLField(null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.allmovie')),
            ],
        ),
        migrations.CreateModel(
            name='AllGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_ids', models.CharField(max_length=50, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.allmovie')),
            ],
        ),
    ]