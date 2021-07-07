# Generated by Django 3.0.3 on 2021-04-19 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='created_time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='modified_time')),
                ('artist_name', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='created_time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='modified_time')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('is_public', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='created_time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='modified_time')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('refresh_token', models.TextField(default='None')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Radio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='created_time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='modified_time')),
                ('name', models.TextField()),
                ('genre_id', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='created_time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='modified_time')),
                ('song_id', models.TextField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('album', models.TextField()),
                ('danceability', models.TextField()),
                ('energy', models.FloatField()),
                ('key', models.IntegerField()),
                ('loudness', models.FloatField()),
                ('mode', models.IntegerField()),
                ('speechiness', models.FloatField()),
                ('acousticness', models.FloatField()),
                ('instrumentalness', models.FloatField()),
                ('liveness', models.FloatField()),
                ('valence', models.FloatField()),
                ('tempo', models.FloatField()),
                ('duration_ms', models.IntegerField()),
                ('time_signature', models.IntegerField()),
                ('img_640', models.TextField(default='https://imgur.com/a/RMIhpXF')),
                ('artists', models.ManyToManyField(related_name='song_artists', to='mainsite.Artist')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserSongPlay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='created_time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='modified_time')),
                ('listened_at', models.DateTimeField(auto_now_add=True)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserPlaylistPlay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='created_time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='modified_time')),
                ('listened_at', models.DateTimeField(auto_now_add=True)),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Playlist')),
                ('radio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Radio')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserGenreSeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='created_time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='modified_time')),
                ('genre_id', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserArtistSeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='created_time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='modified_time')),
                ('artist_id', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SongPlaylist',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='created_time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='modified_time')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Playlist')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Song')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='disliked_songs',
            field=models.ManyToManyField(blank=True, related_name='profile_disliked', to='mainsite.Song'),
        ),
        migrations.AddField(
            model_name='profile',
            name='favorite_playlists',
            field=models.ManyToManyField(blank=True, related_name='profile_favorite_playlists', to='mainsite.Playlist'),
        ),
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='profile_following', to='mainsite.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='liked_songs',
            field=models.ManyToManyField(blank=True, related_name='profile_liked', to='mainsite.Song'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Profile'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(blank=True, through='mainsite.SongPlaylist', to='mainsite.Song'),
        ),
    ]
