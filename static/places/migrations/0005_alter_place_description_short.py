from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0004_load_images"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="description_short",
            field=models.TextField(verbose_name="Краткое описание"),
        ),
    ]