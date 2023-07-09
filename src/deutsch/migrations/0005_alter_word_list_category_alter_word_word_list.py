# Generated by Django 4.2.2 on 2023-07-03 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deutsch', '0004_alter_word_list_category_alter_word_word_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='list_category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='words', to='deutsch.listcategory'),
        ),
        migrations.AlterField(
            model_name='word',
            name='word_list',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='words', to='deutsch.wordlist'),
        ),
    ]