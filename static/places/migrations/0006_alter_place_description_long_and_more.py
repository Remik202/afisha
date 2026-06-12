from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0005_alter_place_description_short"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="description_long",
            field=models.TextField(blank=True, verbose_name="Полное описание"),
        ),
        migrations.AlterField(
            model_name="place",
            name="description_short",
            field=models.TextField(
                blank=True, verbose_name="Краткое описание"
            ),
        ),
    ]