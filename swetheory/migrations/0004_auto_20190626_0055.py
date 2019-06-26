# Generated by Django 2.0.9 on 2019-06-26 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swetheory', '0003_auto_20190626_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cause',
            name='observed_value_c',
            field=models.ForeignKey(blank=True, help_text='Observed values is optional', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cause_obs', to='swetheory.Value'),
        ),
        migrations.AlterField(
            model_name='cause',
            name='reference_value_c',
            field=models.ForeignKey(blank=True, help_text='Reference values is optional', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cause_ref', to='swetheory.Value'),
        ),
        migrations.AlterField(
            model_name='effect',
            name='observed_value',
            field=models.ForeignKey(blank=True, help_text='Observed values is optional', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='effect_obs', to='swetheory.Value'),
        ),
    ]