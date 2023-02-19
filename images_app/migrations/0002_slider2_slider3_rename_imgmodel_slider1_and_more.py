# Generated by Django 4.1.7 on 2023-02-19 14:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("images_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Slider2",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pic", models.ImageField(upload_to="media")),
            ],
            options={
                "verbose_name": "Картинка для второго слайдера",
                "verbose_name_plural": "Картинки для второго слайдера",
            },
        ),
        migrations.CreateModel(
            name="Slider3",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pic", models.ImageField(upload_to="media")),
            ],
            options={
                "verbose_name": "Картинка для третьего слайдера",
                "verbose_name_plural": "Картинки для третьего слайдера",
            },
        ),
        migrations.RenameModel(
            old_name="ImgModel",
            new_name="Slider1",
        ),
        migrations.AlterModelOptions(
            name="slider1",
            options={
                "verbose_name": "Картинка для первого слайдера",
                "verbose_name_plural": "Картинки для первого слайдера",
            },
        ),
    ]
