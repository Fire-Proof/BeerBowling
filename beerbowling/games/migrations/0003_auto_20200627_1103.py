# Generated by Django 3.0.6 on 2020-06-27 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_gameevent_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameevent',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='games.Game'),
        ),
    ]
