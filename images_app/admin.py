from django.contrib import admin

from images_app.models import (
    ImgModel,
    Slider1,
    Slider2,
    Slider3
)


admin.site.register([Slider1, Slider2, Slider3])
