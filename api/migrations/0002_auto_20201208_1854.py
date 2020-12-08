# Generated by Django 3.1.3 on 2020-12-08 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manages',
            old_name='manage_id',
            new_name='collectible_id',
        ),
        migrations.AlterField(
            model_name='deals_with',
            name='adminUsername',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adminUsernameDealsWith', to='api.admin'),
        ),
        migrations.AlterField(
            model_name='manages',
            name='adminUsername',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adminUsernameManages', to='api.admin'),
        ),
        migrations.AlterField(
            model_name='moderates',
            name='adminUsername',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adminUsernameModerates', to='api.admin'),
        ),
        migrations.AlterUniqueTogether(
            name='manages',
            unique_together={('collectible_id', 'adminUsername')},
        ),
    ]
