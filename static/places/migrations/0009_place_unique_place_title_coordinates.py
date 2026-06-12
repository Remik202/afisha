from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0008_alter_image_place_and_more"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="place",
            constraint=models.UniqueConstraint(
                fields=("title", "lng", "lat"),
                name="unique_place_title_coordinates",
            ),
        ),
    ]